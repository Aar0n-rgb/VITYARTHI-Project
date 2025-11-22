import time
import tracemalloc

def collatz_length(n):
    """Returns the number of steps in the Collatz sequence starting from n."""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1  # increment inside the loop
    return steps

def measure_performance(func, n):
    """Measures execution time and peak memory usage of a function."""
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = func(n)
    
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    exec_time = end_time - start_time
    mem_used = peak / 1024  # KB
    return result, exec_time, mem_used

# Example usage
n = 900
length, exec_time, mem_used = measure_performance(collatz_length, n)
print(f"Collatz sequence length for {n}: {length}")
print(f"Execution time: {exec_time:.6f} sec, Peak memory: {mem_used:.2f} KB")
