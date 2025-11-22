import time
import tracemalloc

def partition_function(n):
    """Computes the number of integer partitions of n."""
    tracemalloc.start()
    start_time = time.perf_counter()

    partitions = [0] * (n + 1)
    partitions[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Execution time: {end_time - start_time:.6f} seconds")
    print(f"Peak memory usage: {peak / 1024:.2f} KiB")

    return partitions[n]

# Example usage
n = 100
print(f"Number of partitions of {n}: {partition_function(n)}")
