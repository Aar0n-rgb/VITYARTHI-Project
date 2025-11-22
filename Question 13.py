def is_prime(n):
    """Simple primality test."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_mersenne_prime(p):
    """Returns True if 2^p - 1 is a Mersenne prime."""
    if not is_prime(p):
        return False
    m = 2**p - 1
    return is_prime(m)

if __name__ == "__main__":
    p = int(input("Enter p to test whether 2^p - 1 is a Mersenne prime: "))
    if is_mersenne_prime(p):
        print(f"2^{p} - 1 IS a Mersenne prime!")
    else:
        print(f"2^{p} - 1 is NOT a Mersenne prime.")
