def gcd(a, b):
    """
    Helper: Calculates the Greatest Common Divisor (GCD)
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def order_mod(a, n):
    """
    Finds the smallest positive integer k such that a^k ≡ 1 mod n.
    """
    # The order is only defined if a and n are coprime
    if n <= 1 or gcd(a, n) != 1:
        return None
    
    k = 1
    current_power = a % n
    
    # By Euler's theorem, the order k must be a divisor of phi(n),
    # and phi(n) <= n-1. So, we only need to check up to n.
    while k <= n:
        if current_power == 1:
            return k
        
        # Calculate the next power
        current_power = (current_power * a) % n
        k += 1
        
    return None # Should not be reached if gcd(a, n) == 1
a = 2
n = 7

k = order_mod(a, n)
if k is None:
    print(f"The order of {a} modulo {n} is undefined.")
else:
    print(f"The order of {a} modulo {n} is {k}.")