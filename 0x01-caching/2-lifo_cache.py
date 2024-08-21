#!/usr/bin/env python3
"""
LIFO Caching System
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching System
    """

    def __init__(self):
        """
        Initialize the LIFO cache.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.
        If the key or item is None, the method does nothing.
        If the number of items in the cache exceeds the maximum,
        the newest item is discarded following the LIFO algorithm.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        self.keys.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.keys.pop()
            print(f"DISCARD: {discard_key}")
            del self.cache_data[discard_key]

    def get(self, key):
        """
        Retrieves the value associated with the given key.
        If the key is None or does not exist in the cache, returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
