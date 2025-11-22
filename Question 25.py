def is_prime(n):
    """Helper: Checks if a number n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    # Check divisors up to the square root of n
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_fibonacci(n):
    """Helper: Checks if a number n is a Fibonacci number."""
    if n < 0:
        return False
    if n == 0:
        return True
    
    a, b = 0, 1
    # Generate Fibonacci numbers until we reach or exceed n
    while b < n:
        a, b = b, a + b
    
    # n is Fibonacci if the generated number b is equal to n
    return b == n

def is_fibonacci_prime(n):
    """
    Checks if a number n is both a Fibonacci number and a prime number.
    """
    # We can check prime first, as it's often faster to fail.
    return is_prime(n) and is_fibonacci(n)
n = 4

if is_fibonacci_prime(n):
    print(f"{n} is a Fibonacci prime!")
else:
    print(f"{n} is NOT a Fibonacci prime.")