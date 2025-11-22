def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def twin_primes(limit):
    twins = []
    for p in range(2, limit):
        if is_prime(p) and is_prime(p + 2):
            twins.append((p, p + 2))
    return twins

if __name__ == "__main__":
    n = int(input("Enter limit: "))
    print(twin_primes(n))
