#!/usr/bin/env python3
"""MRUCache module"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """MRU (Most Recently Used) caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.usage_order = []  # List to track the order of key usage

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        # If the key is already in the cache, remove it to update its position later
        if key in self.cache_data:
            self.usage_order.remove(key)

        # Add or update the cache data
        self.cache_data[key] = item
        self.usage_order.append(key)

        # Handle MRU removal if necessary
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # The most recently used item is the last one in usage_order
            mru_key = self.usage_order.pop(-2)  # Discard the second last item in the list
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Update the usage order because this key was accessed
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]

