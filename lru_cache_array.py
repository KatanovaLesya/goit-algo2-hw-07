import random
import time
from functools import lru_cache

# Без кешу

def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])

def update_no_cache(array, index, value):
    array[index] = value


# З кешем

def make_range_sum_with_cache(array):
    @lru_cache(maxsize=1000)
    def cached_sum(L, R):
        return sum(array[L:R+1])
    return cached_sum

def update_with_cache(array, index, value, cached_sum):
    array[index] = value
    cached_sum.cache_clear()  
