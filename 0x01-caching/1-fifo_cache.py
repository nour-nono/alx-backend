#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        # self.cache_data = OrderedDict()
        self .ls = deque()

    # def put(self, key, item):
    #     """Adds an item in the cache.
    #     """
    #     if key and item:
    #         self.cache_data[key] = item
    #     if len(self.cache_data) > BaseCaching.MAX_ITEMS:
    #         first_key, _ = self.cache_data.popitem(False)
    #         print("DISCARD:", first_key)

    # def get(self, key):
    #     """Retrieves an item by key.
    #     """
    #     return self.cache_data.get(key, None)
    def put(self, key, item):
        """ Add an item in the cache
        """
        if not (key and item):
            return
        if self.MAX_ITEMS == len(self.cache_data):
            x = self.ls.popleft()
            self.cache_data.pop(x, 0)
            print("DISCARD:", x)
        self.ls.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
