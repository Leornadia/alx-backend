#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Caching System
    """

    def __init__(self):
        """
        Initialize the MRU cache.
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.
        If the key or item is None, the method does nothing.
        If the number of items in the cache exceeds the maximum,
        the most recently used item is discarded following the MRU algorithm.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_order.remove(key)
        self.mru_order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_recent_key = self.mru_order.pop(0)
            print(f"DISCARD: {most_recent_key}")
            del self.cache_data[most_recent_key]

    def get(self, key):
        """
        Retrieves the value associated with the given key.
        If the key is None or does not exist in the cache, returns None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
