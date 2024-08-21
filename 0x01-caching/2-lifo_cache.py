#!/usr/bin/env python3
"""LIFOCache module"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.last_key = None  # Track the last key inserted for LIFO behavior

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        # Add or update the cache data
        self.cache_data[key] = item
        # Handle LIFO removal if necessary
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")
        # Update last_key to the current key
        self.last_key = key

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
