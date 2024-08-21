#!/usr/bin/env python3
"""LRUCache module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        """Initialize the class with parent's init method"""
        super().__init__()
        self.lru_order = []  # List to maintain the order of usage

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and move the key to the end of the LRU order
            self.cache_data[key] = item
            self.lru_order.remove(key)
            self.lru_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the least recently used item
                lru_key = self.lru_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            # Add the new item and update the LRU order
            self.cache_data[key] = item
            self.lru_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        # Update the LRU order since this key was recently used
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]

