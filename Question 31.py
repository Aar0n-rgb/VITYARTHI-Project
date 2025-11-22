import random
import time
import tracemalloc

def is_prime_miller_rabin(n, k=5):
    """Miller-Rabin primality test with performance measurement."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as d*2^r
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Performance measurement starts
    tracemalloc.start()
    start = time.perf_counter()

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
            end = time.perf_counter()
            curr, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"Time: {end - start:.6f}s, Memory: {peak / 1024:.2f} KiB")
            return False

    # Probably prime
    end = time.perf_counter()
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Time: {end - start:.6f}s, Memory: {peak / 1024:.2f} KiB")
    return True

# Example usage
n = 15485863  # a large prime
print(f"{n} is prime? {is_prime_miller_rabin(n)}")
