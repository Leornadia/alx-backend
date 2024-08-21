#!/usr/bin/env python3
"""
LRU Caching System
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Caching System
    """

    def __init__(self):
        """
        Initialize the LRU cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.
        If the key or item is None, the method does nothing.
        If the number of items in the cache exceeds the maximum,
        the least recently used item is discarded following the LRU algorithm.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_recent_key = next(iter(self.cache_data))
            print(f"DISCARD: {least_recent_key}")
            del self.cache_data[least_recent_key]

    def get(self, key):
        """
        Retrieves the value associated with the given key.
        If the key is None or does not exist in the cache, returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
