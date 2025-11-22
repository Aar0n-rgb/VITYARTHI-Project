import time
import tracemalloc

def zeta_approx(s, terms):
    """Approximates the Riemann zeta function ζ(s) using a finite sum."""
    tracemalloc.start()
    t0 = time.perf_counter()

    z = 0
    for n in range(1, terms + 1):
        z += 1 / (n ** s)

    t1 = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Time: {t1 - t0:.6f}s, Memory: {peak / 1024:.2f} KB")
    return z

# Example usage
s = 2
terms = 100000
approx = zeta_approx(s, terms)
print(f"ζ({s}) ≈ {approx:.6f}")
