import timeit
import matplotlib.pyplot as plt
from functools import lru_cache
from fibonacci_splay import SplayTree


@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_splay(n, tree: SplayTree):
    cached = tree.get(n)
    if cached is not None:
        return cached
    if n < 2:
        result = n
    else:
        result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result


def run_tests():
    test_values = list(range(0, 951, 50))
    lru_times = []
    splay_times = []

    for n in test_values:
        # LRU
        lru_timer = timeit.repeat(lambda: fibonacci_lru(n), number=1, repeat=5)
        lru_avg = sum(lru_timer) / len(lru_timer)
        lru_times.append(lru_avg)

        # Splay
        tree = SplayTree()
        splay_timer = timeit.repeat(lambda: fibonacci_splay(n, tree), number=1, repeat=5)
        splay_avg = sum(splay_timer) / len(splay_timer)
        splay_times.append(splay_avg)

        print(f"{n:<10} {lru_avg:.10f}     {splay_avg:.10f}")

    return test_values, lru_times, splay_times


def plot_graph(xs, lru, splay):
    plt.figure(figsize=(10, 6))
    plt.plot(xs, lru, label='LRU Cache')
    plt.plot(xs, splay, label='Splay Tree')
    plt.xlabel("n (Fibonacci number index)")
    plt.ylabel("Average time (s)")
    plt.title("Fibonacci: LRU Cache vs Splay Tree")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print(f"{'n':<10}{'LRU Cache Time (s)':<20}Splay Tree Time (s)")
    print("-" * 50)
    xs, lru_t, splay_t = run_tests()
    plot_graph(xs, lru_t, splay_t)
