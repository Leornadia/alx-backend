#!/usr/bin/env python3
"""MRUCache module"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """MRU (Most Recently Used) caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.mru_order = []  # Track the order of access (MRU order)

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        # Add or update the cache data
        self.cache_data[key] = item

        # Update mru_order (handle existing key and append)
        if key in self.mru_order:
            self.mru_order.remove(key)
        self.mru_order.append(key)

        # Handle MRU removal if necessary
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order.pop(0)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            # Update mru_order (remove and re-append)
            self.mru_order.remove(key)
            self.mru_order.append(key)
        return self.cache_data.get(key, None)
