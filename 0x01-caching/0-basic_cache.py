#!/usr/bin/env python3
"""This module contains a basic caching class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class definition"""
    def __init__(self):
        """Instantiation method"""
        super().__init__()

    def put(self, key, item):
        """This method adds a key value pair to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """This method returns value associated with 'key' in cache"""
        return self.cache_data.get(key)
