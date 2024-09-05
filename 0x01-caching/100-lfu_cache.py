#!/usr/bin/env python3
"""Inherits from BaseCaching and is a chaching system."""

from collections import OrderedDict
from base_caching import BaseCaching
import time

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Implements LFU caching."""

    def __init__(self):
        """Initialize by overloading parent's initialization."""
        self.counter = {}  # counter for frequency of use
        self.ordered_dict = OrderedDict()  # for recent access monitoring
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value
         for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS:
        you must discard the least frequency used item (LFU algorithm)
        if you find more than 1 item to discard,
        you must use the LRU algorithm to discard only the least recently used
        you must print DISCARD: with the key discarded
        and following by a new line
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.counter[key] = self.counter.get(key, 0) + 1
                self.ordered_dict.move_to_end(key)  # update recent access
                self.cache_data[key] = item

            elif len(self.cache_data) >= self.MAX_ITEMS:
                least_freq = min(self.counter.values())
                items_with_least_freq = [
                    k for k, v in self.counter.items() if v == least_freq
                ]
                lru_item = min(
                    items_with_least_freq,
                    key=lambda k: self.ordered_dict.get(k, 0)
                )
                self.cache_data.pop(lru_item)
                self.counter.pop(lru_item)
                self.ordered_dict.pop(lru_item)
                self.cache_data[key] = item
                self.counter[key] = 1
                self.ordered_dict[key] = time.time()
                print(f"DISCARD: {lru_item}")
            else:
                self.cache_data[key] = item
                self.counter[key] = 1
                self.ordered_dict[key] = time.time()

    def get(self, key):
        """Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key in self.cache_data.keys():
            self.counter[key] += 1
            self.ordered_dict.move_to_end(key)
            return self.cache_data.get(key)
        return None
