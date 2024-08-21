#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements a LIFO
    caching system.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance.
        """
        super().__init__()
        self.lifo_order = []  # List to keep track of LIFO order

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key for the item.
            item (any): The item to store.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lifo_order.remove(key)  # Update order if key exists

        self.cache_data[key] = item
        self.lifo_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.lifo_order.pop()
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

    def get(self, key):
        """
        Get an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item associated with the key or None if not found.
        """
        return self.cache_data.get(key)
