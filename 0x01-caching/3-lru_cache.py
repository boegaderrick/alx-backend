#!/usr/bin/env python3
"""This module contains LRUCache class"""
from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """Class definition"""
    def __init__(self):
        """Initialization method"""
        super().__init__()
        self.__timestamps = {}

    def get(self, key):
        """This method returns value associated with 'key'"""
        value = self.cache_data.get(key)
        if value:
            self.__timestamps[key] = datetime.now()
            return value

    def put(self, key, item):
        """
            This method takes two parameters ['key' & 'item'] and
            pairs them in the cache_data dictionary of the class.
            If the total number of items stored in the dictionary
            exceed the limit set by the parent class' 'MAX_ITEMS'
            attribute, the least recently used item in the
            dictionary is purged.
        """
        if key and item:
            self.cache_data[key] = item
            self.__timestamps[key] = datetime.now()
            if len(self.cache_data) > self.MAX_ITEMS:
                lruKey = self.get_lru()
                print('DISCARD: {}'.format(lruKey))
                del self.cache_data[lruKey]
                del self.__timestamps[lruKey]

    def get_lru(self):
        """Helper method to retrieve the least recently used key"""
        lru = None
        for key, item in self.__timestamps.items():
            if lru is None:
                lru = key
                continue
            if item < self.__timestamps[lru]:
                lru = key

        return lru
