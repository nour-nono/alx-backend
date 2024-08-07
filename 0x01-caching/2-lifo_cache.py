#!/usr/bin/env python3
"""Last-In First-Out caching module.
"""
from collections import OrderedDict
# from collections import deque

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        # self .ls = deque()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
    # def put(self, key, item):
    #     """ Add an item in the cache
    #     """
    #     if not (key and item):
    #         return
    #     if self.MAX_ITEMS == len(self.cache_data):
    #         x = self.ls.pop()
    #         self.cache_data.pop(x, 0)
    #         print("DISCARD:", x)
    #     self.ls.append(key)
    #     self.cache_data[key] = item

    # def get(self, key):
    #     """ Get an item by key
    #     """
    #     return self.cache_data.get(key, None)
