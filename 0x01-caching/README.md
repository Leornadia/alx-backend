# 0x01. Caching

## Description

This project involves implementing different caching algorithms in Python. A caching system stores data temporarily to serve future requests more quickly. The cache can be designed with various replacement policies to manage which data should be kept and which should be removed when the cache reaches its capacity.

## Learning Objectives

By the end of this project, you should be able to:

- Understand what a caching system is.
- Explain the following cache replacement policies:
  - FIFO (First-In, First-Out)
  - LIFO (Last-In, First-Out)
  - LRU (Least Recently Used)
  - MRU (Most Recently Used)
  - LFU (Least Frequently Used)
- Understand the purpose of a caching system.
- Discuss the limitations of a caching system.

## Caching Algorithms Implemented

### 1. FIFO Cache (First-In, First-Out)
The `FIFOCache` class implements a cache that evicts the oldest entry when it reaches its limit.

### 2. LIFO Cache (Last-In, First-Out)
The `LIFOCache` class implements a cache that evicts the most recent entry when it reaches its limit.

### 3. LRU Cache (Least Recently Used)
The `LRUCache` class implements a cache that evicts the least recently used entry when it reaches its limit.

### 4. MRU Cache (Most Recently Used)
The `MRUCache` class implements a cache that evicts the most recently used entry when it reaches its limit.

### 5. LFU Cache (Least Frequently Used)
The `LFUCache` class implements a cache that evicts the least frequently used entry when it reaches its limit.

## Project Structure

- **base_caching.py**: Contains the `BaseCaching` class which defines the base structure and constants for the caching system.
- **fifo_cache.py**: Contains the `FIFOCache` class.
- **lifo_cache.py**: Contains the `LIFOCache` class.
- **lru_cache.py**: Contains the `LRUCache` class.
- **mru_cache.py**: Contains the `MRUCache` class.
- **lfu_cache.py**: Contains the `LFUCache` class.

## Requirements

- Python 3.7 is used to run all scripts.
- All scripts should conform to the `pycodestyle` style guide.
- Each script is executable and contains appropriate shebang (`#!/usr/bin/env python3`).
- All classes and methods are well-documented with appropriate docstrings.

## Usage

To use any of the caching algorithms, simply import the desired class from its corresponding script and use the `put` and `get` methods to interact with the cache.

Example usage for FIFO Cache:

```python
from fifo_cache import FIFOCache

my_cache = FIFOCache()

my_cache.put("A", "Value A")
my_cache.put("B", "Value B")
my_cache.put("C", "Value C")
my_cache.put("D", "Value D")

print(my_cache.get("A"))  # Outputs: Value A

my_cache.put("E", "Value E")  # This will evict the first entry ("A")
print(my_cache.get("A"))  # Outputs: None

