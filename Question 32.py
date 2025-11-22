import random
import time
import tracemalloc

def is_prime_miller_rabin(n, k=5):
    """Miller-Rabin primality test with time and memory measurement."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # write n-1 as d*2^r
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Start performance measurement
    tracemalloc.start()
    t0 = time.perf_counter()

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # Composite
            t1 = time.perf_counter()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"Time: {t1 - t0:.6f}s, Memory: {peak / 1024:.2f} KB")
            return False

    # Probably prime
    t1 = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Time: {t1 - t0:.6f}s, Memory: {peak / 1024:.2f} KB")
    return True

# Example usage
n = 15485863  # a large prime
print(f"{n} is prime? {is_prime_miller_rabin(n)}")
