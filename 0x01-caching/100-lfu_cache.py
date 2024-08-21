#!/usr/bin/env python3
"""LFUCache module"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """LFU (Least Frequently Used) caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.frequency = {}  # Dictionary to store the frequency of each key
        self.usage_order = []  # List to track the order of key usage

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        # If the key already exists, update its value and increment its frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # If the cache is full, remove the least frequently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
                
                # If there's a tie (multiple items with the same frequency), use LRU to break the tie
                if len(lfu_keys) > 1:
                    for k in self.usage_order:
                        if k in lfu_keys:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]
                
                # Remove the LFU (and LRU in case of tie) key
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new item
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Increment the frequency of the accessed item
        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]

