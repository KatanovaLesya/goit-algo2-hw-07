import random
import time
from lru_cache_array import (
    range_sum_no_cache,
    update_no_cache,
    make_range_sum_with_cache,
    update_with_cache
)

N = 100_000
Q = 50_000
RANGE_POOL_SIZE = 100  

array = [random.randint(1, 1000) for _ in range(N)]

range_pool = [
    (random.randint(0, N - 2), random.randint(0, N - 1))
    for _ in range(RANGE_POOL_SIZE)
]

queries = []
for _ in range(Q):
    if random.random() < 0.9:  
        L, R = random.choice(range_pool)
        if L > R:
            L, R = R, L
        queries.append(('Range', L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 1000)
        queries.append(('Update', index, value))

array_no_cache = array.copy()
start = time.perf_counter()
for q in queries:
    if q[0] == 'Range':
        range_sum_no_cache(array_no_cache, q[1], q[2])
    else:
        update_no_cache(array_no_cache, q[1], q[2])
end = time.perf_counter()
print(f"Час виконання без кешування: {end - start:.2f} секунд")

array_with_cache = array.copy()
cached_sum = make_range_sum_with_cache(array_with_cache)

start = time.perf_counter()
for q in queries:
    if q[0] == 'Range':
        cached_sum(q[1], q[2])
    else:
        update_with_cache(array_with_cache, q[1], q[2], cached_sum)
end = time.perf_counter()
print(f"Час виконання з LRU-кешем: {end - start:.2f} секунд")
