#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements an MRU
    caching system.
    """

    def __init__(self):
        """
        Initialize the MRUCache instance.
        """
        super().__init__()
        self.mru_order = []  # List to keep track of MRU order

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
            self.mru_order.remove(key)  # Update order if key exists

        self.cache_data[key] = item
        self.mru_order.append(key)  # Add key to the end (most recently used)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order.pop(0)  # Remove the least recently used
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

    def get(self, key):
        """
        Get an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item associated with the key or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end of the MRU order when it's accessed
        self.mru_order.remove(key)
        self.mru_order.append(key)

        return self.cache_data[key]
