#!/usr/bin/env python3
"""This module contains MRUCache class"""
from base_caching import BaseCaching
from datetime import datetime


class MRUCache(BaseCaching):
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
            attribute, the most recently used item in the
            dictionary is purged.
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                mruKey = self.get_mru()
                print('DISCARD: {}'.format(mruKey))
                del self.cache_data[mruKey]
                del self.__timestamps[mruKey]
            self.__timestamps[key] = datetime.now()

    def get_mru(self):
        """Helper method to retrieve the most recently used key"""
        mru = None
        for key, item in self.__timestamps.items():
            if mru is None:
                mru = key
                continue
            if item > self.__timestamps[mru]:
                mru = key

        return mru
