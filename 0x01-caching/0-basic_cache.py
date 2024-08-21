#!/usr/bin/env python3
"""
Basic Caching System
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching System
    """

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.
        If the key or item is None, the method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key.
        If the key is None or does not exist in the cache, returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
