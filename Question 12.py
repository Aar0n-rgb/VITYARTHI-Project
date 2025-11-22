def is_prime_power(n):
    if n <= 1:
        return False

    for p in range(2, int(n**0.5) + 2):
        if n % p == 0:
            k = 0
            x = n
            while x % p == 0:
                x //= p
                k += 1
            if x == 1 and k >= 1:
                return True
    return n > 1 
n=7
print(is_prime_power(n))
