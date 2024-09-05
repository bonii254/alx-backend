#!/usr/bin/env python3
"""a class LRUCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching and is a caching system
       implementing the Least Recently Used (LRU) caching algorithm.

       Methods:
           put(key, item):
               Add an item to the cache. If the cache exceeds its limit,
               evicts the least recently used item.

           get(key):
               Retrieve an item from the cache. If the key exists,
               it is marked as recently used.
    """

    def __init__(self):
        """
        Initialize the LRUCache with the parent class attributes and
        create an OrderedDict to maintain the order of the cache items.
        """
        super().__init__()
        self.ordered_dict = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache with the specified key.
        If the number of items in the cache exceeds the limit defined by
        BaseCaching.MAX_ITEMS, the least recently used (LRU) item is discarded.

        Args:
            key: The key associated with the item to be added to the cache.
            item: The item to be added to the cache.

        Returns:
            None. If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.ordered_dict.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed_item = self.ordered_dict.popitem(last=False)
            self.cache_data.pop(removed_item[0])
            print(f"DISCARD: {removed_item[0]}")
        self.cache_data[key] = item
        self.ordered_dict[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache with the specified key.
        If the key exists in the cache, it is marked as recently used by
        moving it to the end of the cache.
        If the key does not exist, return None

        Args:
            key: The key of the item to retrieve from the cache.

        Returns:
            The value associated with the key,
            or None if the key does not exist..
        """
        if key in self.cache_data:
            self.ordered_dict.move_to_end(key)
            return self.cache_data.get(key)
        return None
