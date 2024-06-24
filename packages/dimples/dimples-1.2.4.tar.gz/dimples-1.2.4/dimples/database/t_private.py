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

from typing import Optional, List

from dimsdk import DateTime
from dimsdk import PrivateKey, DecryptKey, SignKey
from dimsdk import ID

from ..utils import CacheManager
from ..common import PrivateKeyDBI

from .dos import PrivateKeyStorage


class PrivateKeyTable(PrivateKeyDBI):
    """ Implementations of PrivateKeyDBI """

    # CACHE_EXPIRES = 300  # seconds
    CACHE_REFRESHING = 32  # seconds

    def __init__(self, root: str = None, public: str = None, private: str = None):
        super().__init__()
        self.__dos = PrivateKeyStorage(root=root, public=public, private=private)
        man = CacheManager()
        self.__id_key_cache = man.get_pool(name='private_id_key')      # ID => PrivateKey
        self.__msg_keys_cache = man.get_pool(name='private_msg_keys')  # ID => List[PrivateKey]

    def show_info(self):
        self.__dos.show_info()

    async def _add_decrypt_key(self, key: PrivateKey, user: ID) -> Optional[List[PrivateKey]]:
        private_keys = await self.private_keys_for_decryption(user=user)
        private_keys = PrivateKeyDBI.convert_private_keys(keys=private_keys)
        return PrivateKeyDBI.insert(item=key, array=private_keys)

    #
    #   Private Key DBI
    #

    # Override
    async def save_private_key(self, key: PrivateKey, user: ID, key_type: str = 'M') -> bool:
        now = DateTime.now()
        # 1. update memory cache
        if key_type == PrivateKeyStorage.ID_KEY_TAG:
            # update 'id_key'
            self.__id_key_cache.update(key=user, value=key, life_span=36000, now=now)
        else:
            # add to old keys
            private_keys = self._add_decrypt_key(key=key, user=user)
            if private_keys is None:
                # key already exists, nothing changed
                return False
            # update 'msg_keys'
            self.__msg_keys_cache.update(key=user, value=private_keys, life_span=36000, now=now)
        # 2. update local storage
        return await self.__dos.save_private_key(key=key, user=user, key_type=key_type)

    # Override
    async def private_keys_for_decryption(self, user: ID) -> List[DecryptKey]:
        """ get sign key for ID """
        now = DateTime.now()
        # 1. check memory cache
        value, holder = self.__msg_keys_cache.fetch(key=user, now=now)
        if value is None:
            # cache empty
            if holder is None:
                # cache not load yet, wait to load
                self.__msg_keys_cache.update(key=user, life_span=self.CACHE_REFRESHING, now=now)
            else:
                if holder.is_alive(now=now):
                    # cache not exists
                    return []
                # cache expired, wait to reload
                holder.renewal(duration=self.CACHE_REFRESHING, now=now)
            # 2. check local storage
            value = await self.__dos.private_keys_for_decryption(user=user)
            # 3. update memory cache
            if value is None:
                self.__msg_keys_cache.update(key=user, value=value, life_span=300, now=now)
            else:
                self.__msg_keys_cache.update(key=user, value=value, life_span=36000, now=now)
        # OK, return cached value
        return value

    # Override
    async def private_key_for_signature(self, user: ID) -> Optional[SignKey]:
        # TODO: support multi private keys
        return await self.private_key_for_visa_signature(user=user)

    # Override
    async def private_key_for_visa_signature(self, user: ID) -> Optional[SignKey]:
        """ get sign key for ID """
        now = DateTime.now()
        # 1. check memory cache
        value, holder = self.__id_key_cache.fetch(key=user, now=now)
        if value is None:
            # cache empty
            if holder is None:
                # cache not load yet, wait to load
                self.__id_key_cache.update(key=user, life_span=self.CACHE_REFRESHING, now=now)
            else:
                if holder.is_alive(now=now):
                    # cache not exists
                    return None
                # cache expired, wait to reload
                holder.renewal(duration=self.CACHE_REFRESHING, now=now)
            # 2. check local storage
            value = await self.__dos.private_key_for_visa_signature(user=user)
            # 3. update memory cache
            if value is None:
                self.__id_key_cache.update(key=user, value=value, life_span=600, now=now)
            else:
                self.__id_key_cache.update(key=user, value=value, life_span=36000, now=now)
        # OK, return cached value
        return value
