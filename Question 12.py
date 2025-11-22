def is_prime_power(n):
    if n <= 1:
        return False

    for p in range(2, int(n**0.5) + 2):
        k = 0
        x = n
        while x % p == 0:
            x //= p
            k += 1
        if x == 1 and k >= 1:
            return True

    # If n itself is prime, it's a prime power (n = n^1)
    from math import isqrt
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
n = 7
print(is_prime_power(n))  

n = 8
print(is_prime_power(n))  

n = 6
print(is_prime_power(n))  

