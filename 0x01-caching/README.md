# ALX Backend Caching Project

This project explores various caching algorithms for optimizing backend performance, including FIFO, LIFO, LRU, MRU, and LFU caching.

## Table of Contents
- [Overview](#overview)
- [BaseCaching Class](#basecaching-class)
- [Caching Systems](#caching-systems)
- [BasicCache](#basiccache)
- [FIFOCache](#fifocache)
- [LIFOCache](#lifocache)
- [LRUCache](#lrucache)
- [MRUCache](#mrucache)
- [LFUCache](#lfucache)

## Overview
In this project, we implement different caching algorithms for effective data retrieval. Each system inherits from `BaseCaching` and implements `put()` and `get()` methods.

## BaseCaching Class
The parent class, `BaseCaching`, defines:
- `cache_data`: Dictionary for storing cache items.
- `MAX_ITEMS`: Max cache size (4 items).

## Caching Systems

### BasicCache
- Unlimited cache with no eviction.

### FIFOCache
- Follows **First-In-First-Out (FIFO)**.
- Discards the oldest item when exceeding `MAX_ITEMS`.

### LIFOCache
- Follows **Last-In-First-Out (LIFO)**.
- Discards the most recent item when exceeding `MAX_ITEMS`.

### LRUCache
- Follows **Least Recently Used (LRU)**.
- Discards the least accessed item.

### MRUCache
- Follows **Most Recently Used (MRU)**.
- Discards the most accessed item.

### LFUCache
- Follows **Least Frequently Used (LFU)**.
- Discards the least frequently accessed item, using LRU as a tiebreaker.

---

