#!/usr/bin/env python3
"""This module contains LFUCache class"""
from base_caching import BaseCaching
from datetime import datetime


class LFUCache(BaseCaching):
    """Class definition"""
    def __init__(self):
        """Initialization method"""
        super().__init__()
        self.__frequency = {}
        self.__timestamps = {}

    def get(self, key):
        """This method returns value associated with 'key'"""
        value = self.cache_data.get(key)
        if value:
            self.__frequency[key] += 1
            self.__timestamps[key] = datetime.now()
            return value

    def put(self, key, item):
        """
            This method takes two parameters ['key' & 'item'] and
            pairs them in the cache_data dictionary of the class.
            If the total number of items stored in the dictionary
            exceeds the limit set by the parent class' 'MAX_ITEMS'
            attribute, the least frequently used item in the
            dictionary is purged.
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                lfuKey = self.get_lfu()
                print('DISCARD: {}'.format(lfuKey))
                del self.cache_data[lfuKey]
                del self.__frequency[lfuKey]
                del self.__timestamps[lfuKey]

            if not self.__frequency.get(key):
                self.__frequency[key] = 1
            else:
                self.__frequency[key] += 1
            self.__timestamps[key] = datetime.now()

    def get_lfu(self):
        """Helper method to retrieve the least frequently used key"""
        lfu = None
        for key, item in self.__frequency.items():
            if lfu is None:
                lfu = key
                continue
            if item < self.__frequency[lfu]:
                lfu = key

        lfuKeyVal = self.__frequency[lfu]
        if list(self.__frequency.values()).count(lfuKeyVal) > 1:
            return self.get_lru(lfuKeyVal)

        return lfu

    def get_lru(self, lfuVal):
        """Helper method to retrieve the least recently used key"""
        lru = None
        for key, item in self.__timestamps.items():
            if self.__frequency[key] == lfuVal:
                if lru is None:
                    lru = key
                    continue
                if item < self.__timestamps[lru]:
                    lru = key

        return lru
