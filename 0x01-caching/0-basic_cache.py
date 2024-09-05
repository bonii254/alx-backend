#!/usr/bin/env python3
"""Module for class BasicCache inheriting from BaseCaching."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system with no limit """

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
        return None
