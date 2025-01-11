#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching.
    This caching system does not have a limit on the number of items.
    """

    def __init__(self):
        """ Initialize the BasicCache class.
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache.

        Args:
            key (str): The key for the cache item.
            item (any): The value to be cached.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache by key.

        Args:
            key (str): The key for the cache item.

        Returns:
            any: The cached value if the key exists, otherwise None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
