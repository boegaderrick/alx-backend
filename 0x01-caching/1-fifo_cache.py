#!/usr/bin/env python3
"""This module contains FIFOCache class"""
from base_caching import BaseCaching
from datetime import datetime


class FIFOCache(BaseCaching):
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
            attribute, the oldest item in the dictionary is purged.
        """
        if key and item:
            self.cache_data[key] = item
            self.__timestamps[key] = datetime.now()
            if len(self.cache_data) > self.MAX_ITEMS:
                key = self.get_oldest()
                print('DISCARD: {}'.format(key))
                del self.cache_data[key]
                del self.__timestamps[key]

    def get_oldest(self):
        """Helper method to retrieve the oldes key"""
        oldest = None
        for key, item in self.__timestamps.items():
            if oldest is None:
                oldest = key
                continue
            if item < self.__timestamps[oldest]:
                oldest = key

        return oldest
