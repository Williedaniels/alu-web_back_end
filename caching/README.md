# BasicCache

A simple caching system that inherits from `BaseCaching` and implements a basic dictionary-based cache without a limit.

## Usage

1. Import the `BasicCache` class.
2. Create an instance of `BasicCache`.
3. Use the `put` method to add items to the cache.
4. Use the `get` method to retrieve items from the cache.

Example:

```python
from basic_cache import BasicCache

bc = BasicCache()
bc.put("key1", "value1")
print(bc.get("key1"))  # Output: value1
