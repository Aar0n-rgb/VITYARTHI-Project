import time
import tracemalloc
import math

def is_perfect_power(n):
    """Returns True if n is a perfect power (a^b) with a > 1, b > 1, else False."""
    if n <= 1:
        return True  # 1 = 1^b is considered a perfect power

    max_b = int(math.log2(n)) + 1  # b must be at most log2(n)
    for b in range(2, max_b + 1):
        a = round(n ** (1 / b))
        if a > 1 and a ** b == n:
            return True
    return False

def measure_performance(func, n):
    """Measures execution time and peak memory usage of a function."""
    tracemalloc.start() 
    start_time = time.perf_counter()
    
    result = func(n)
    
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    exec_time = end_time - start_time
    mem_used = peak / 1024  # memory in KB
    return result, exec_time, mem_used

# Example usage
n = 64
result, exec_time, mem_used = measure_performance(is_perfect_power, n)
print(f"{n} is a perfect power? {result}")
print(f"Execution time: {exec_time:.6f} sec, Peak memory: {mem_used:.2f} KB")
