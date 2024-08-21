#!/usr/bin/env python3
"""MRUCache module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""

    def __init__(self):
        """Initialize the class with parent's init method"""
        super().__init__()
        self.mru_key = None  # To keep track of the most recently used key

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used item
                if self.mru_key is not None:
                    del self.cache_data[self.mru_key]
                    print(f"DISCARD: {self.mru_key}")
            # Add the new item to the cache
            self.cache_data[key] = item

        # Update the most recently used key
        self.mru_key = key

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Update the most recently used key
        self.mru_key = key
        return self.cache_data[key]

