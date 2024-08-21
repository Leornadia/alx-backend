#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and implements an LFU
    caching system with LRU tie-breaker.
    """

    def __init__(self):
        """
        Initialize the LFUCache instance.
        """
        super().__init__()
        self.cache_data = {}  # Dictionary to store cached items
        self.frequency = {}  # Dictionary to track access frequency
        self.access_order = {}  # Dictionary to track access order (LRU tie-breaker)

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
            self.frequency[key] += 1
            self.access_order[key] = len(self.access_order)  # Update LRU order
        else:
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.access_order[key] = len(self.access_order)

        # Handle LFU and LRU eviction if cache is full
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
            lru_key = min(lfu_keys, key=lambda k: self.access_order[k])
            del self.cache_data[lru_key]
            del self.frequency[lru_key]
            del self.access_order[lru_key]
            print(f"DISCARD: {lru_key}")

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

        self.frequency[key] += 1  # Increase frequency on access
        self.access_order[key] = len(self.access_order)  # Update LRU order
        return self.cache_data[key]
