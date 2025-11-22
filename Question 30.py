import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def prime_factors(n):
    """Returns the set of prime factors of n."""
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def is_square_free(n):
    """Checks if n is square-free."""
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % (i * i) == 0:
            return False
    return True

def is_carmichael(n):
    """Checks if n is a Carmichael number."""
    if n < 2 or is_prime(n := n):  # Carmichael numbers are composite
        return False
    if not is_square_free(n):
        return False
    factors = prime_factors(n)
    for p in factors:
        if (n - 1) % (p - 1) != 0:
            return False
    return True

def is_prime(n):
    """Simple primality test for small numbers."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
for n in [561, 1105, 1729, 13]:
    print(f"{n} is Carmichael? {is_carmichael(n)}")
