#!/usr/bin/env python3
"""Least Recently Used caching module.
"""
# from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LRU
    algorithm when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.ls = []
    #     self.cache_data = OrderedDict()

    # def put(self, key, item):
    #     """Adds an item in the cache.
    #     """
    #     if key is None or item is None:
    #         return
    #     if key not in self.cache_data:
    #         if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
    #             lru_key, _ = self.cache_data.popitem(True)
    #             print("DISCARD:", lru_key)
    #         self.cache_data[key] = item
    #         self.cache_data.move_to_end(key, last=False)
    #     else:
    #         self.cache_data[key] = item

    # def get(self, key):
    #     """Retrieves an item by key.
    #     """
    #     if key is not None and key in self.cache_data:
    #         self.cache_data.move_to_end(key, last=False)
    #     return self.cache_data.get(key, None)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not (key and item):
            return
        if key in self.ls:
            self.ls.remove(key)
        else:
            if self.MAX_ITEMS == len(self.cache_data):
                print("DISCARD:", self.cache_data.pop(self.ls.pop(0), 0))
        self.ls.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
