#!/usr/bin/env python3
"""This module contains LIFOCache class"""
from base_caching import BaseCaching
from datetime import datetime


class LIFOCache(BaseCaching):
    """Class definition"""
    def __init__(self):
        """Initialization method"""
        super().__init__()
        self.__timestamps = {}

    def get(self, key):
        """This method returns value associated with 'key'"""
        return self.cache_data.get(key)

    def put(self, key, item):
        """
            This method takes two parameters ['key' & 'item'] and
            pairs them in the cache_data dictionary of the class.
            If the total number of items stored in the dictionary
            exceed the limit set by the parent class' 'MAX_ITEMS'
            attribute, the newest item in the dictionary is purged.
        """
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS:
                if not self.cache_data.get(key):
                    newestKey = self.get_newest()
                    print('DISCARD: {}'.format(newestKey))
                    del self.cache_data[newestKey]
                    del self.__timestamps[newestKey]
            self.cache_data[key] = item
            self.__timestamps[key] = datetime.now()

    def get_newest(self):
        """Helper method to retrieve the newest key"""
        newest = None
        for key, item in self.__timestamps.items():
            if newest is None:
                newest = key
                continue
            if item > self.__timestamps[newest]:
                newest = key

        return newest
