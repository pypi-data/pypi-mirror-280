# -*- coding: utf-8 -*-
# ==============================================================================
# MIT License
#
# Copyright (c) 2022 Albert Moky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

from typing import List

from dimsdk import DateTime
from dimsdk import ID
from dimsdk import ReliableMessage

from ..utils import CacheManager
from ..common import ReliableMessageDBI


class ReliableMessageTable(ReliableMessageDBI):
    """ Implementations of ReliableMessageDBI """

    CACHE_EXPIRES = 3600*24*7  # seconds

    # noinspection PyUnusedLocal
    def __init__(self, root: str = None, public: str = None, private: str = None):
        super().__init__()
        man = CacheManager()
        self.__msg_cache = man.get_pool(name='reliable_messages')  # ID => List[ReliableMessage]

    # noinspection PyMethodMayBeStatic
    def show_info(self):
        print('!!! messages cached in memory only !!!')

    #
    #   Reliable Message DBI
    #

    # Override
    async def get_reliable_messages(self, receiver: ID, limit: int = 1024) -> List[ReliableMessage]:
        now = DateTime.now()
        # get all messages
        messages, _ = self.__msg_cache.fetch(key=receiver, now=now)
        if messages is None:
            return []
        # only last cached messages will be returned
        if 0 < limit < len(messages):
            messages = messages[-limit:]
        return messages

    # Override
    async def cache_reliable_message(self, msg: ReliableMessage, receiver: ID) -> bool:
        now = DateTime.now()
        # assert receiver.is_user, 'message receiver error: %s' % receiver
        messages, holder = self.__msg_cache.fetch(key=receiver, now=now)
        if messages is None:
            messages = [msg]
            self.__msg_cache.update(key=receiver, value=messages, life_span=self.CACHE_EXPIRES, now=now)
            return True
        elif find_message(msg=msg, messages=messages) < 0:
            assert isinstance(messages, List), 'msg cache list error: %s' % messages
            while len(messages) > ReliableMessageDBI.CACHE_LIMIT:
                # overflow
                messages.pop(0)
            # append to tail
            messages.append(msg)
            holder.update(value=messages, now=now)
            return True
        else:
            # duplicated
            return False

    # Override
    async def remove_reliable_message(self, msg: ReliableMessage, receiver: ID) -> bool:
        now = DateTime.now()
        # assert receiver.is_user, 'message receiver error: %s' % receiver
        messages, holder = self.__msg_cache.fetch(key=receiver, now=now)
        if messages is None:
            # not exists
            return False
        index = find_message(msg=msg, messages=messages)
        if index < 0:
            # not exists
            return False
        assert isinstance(messages, list), 'msg list error: %s' % messages
        messages.pop(index)
        holder.update(value=messages, now=now)
        return True


def find_message(msg: ReliableMessage, messages: List[ReliableMessage]) -> int:
    """ check message by signature """
    index = 0
    sig = msg.get('signature')
    for item in messages:
        if item.get('signature') == sig:
            return index
        index += 1
    # not found
    return -1
