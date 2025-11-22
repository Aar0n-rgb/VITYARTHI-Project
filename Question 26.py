import time
import tracemalloc

def lucas_sequence(n):
    """Generates the first n Lucas numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [2]
    
    lucas = [2, 1]
    while len(lucas) < n:
        lucas.append(lucas[-1] + lucas[-2])
    return lucas  # <-- return must be outside the loop

def measure_lucas_performance(n):
    """Measures execution time and memory usage of generating n Lucas numbers."""
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = lucas_sequence(n)
    
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    memory_used = peak / 1024  # memory in KB
    
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Peak memory usage: {memory_used:.2f} KB")
    
    return result

n = 10
lucas_numbers = measure_lucas_performance(n)
print(f"First {n} Lucas numbers: {lucas_numbers}")
