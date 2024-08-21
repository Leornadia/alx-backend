#!/usr/bin/env python3
"""LIFOCache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """Initialize the class with parent's init method"""
        super().__init__()
        self.keys_order = []  # To track the order of keys

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item if the key already exists
            self.cache_data[key] = item
            self.keys_order.remove(key)
            self.keys_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the last item added (LIFO)
                last_key = self.keys_order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            # Add the new item to the cache
            self.cache_data[key] = item
            self.keys_order.append(key)

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)

