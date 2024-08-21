#!/usr/bin/env python3
"""
FIFO Caching System
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching System
    """

    def __init__(self):
        """
        Initialize the FIFO cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.
        If the key or item is None, the method does nothing.
        If the number of items in the cache exceeds the maximum,
        the oldest item is discarded following the FIFO algorithm.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

    def get(self, key):
        """
        Retrieves the value associated with the given key.
        If the key is None or does not exist in the cache, returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
