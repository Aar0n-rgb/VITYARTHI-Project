def power(base, exp, mod):
    """
    Helper: Calculates (base^exp) % mod efficiently
    using exponentiation by squaring (binary exponentiation).
    """
    res = 1
    base %= mod
    while exp > 0:
        # If exponent is odd, multiply result with base
        if exp % 2 == 1:
            res = (res * base) % mod
        
        # Exponent must be even now
        exp = exp >> 1  # equivalent to exp //= 2
        base = (base * base) % mod
    return res

def is_quadratic_residue(a, p):
    """
    Checks if x^2 ≡ a mod p has a solution using Euler's Criterion.
    Assumes p is an odd prime.
    """
    # Handle the trivial case where a is a multiple of p
    if a % p == 0:
        return True  # x = 0 is a solution
    
    # Handle the special case for p = 2
    if p == 2:
        return a % 2 == 1 # Only 1 is a residue mod 2 (1^2 ≡ 1)

    # Euler's Criterion:
    # a is a quadratic residue mod p iff a^((p-1)/2) ≡ 1 (mod p)
    
    exponent = (p - 1) // 2
    legendre_symbol = power(a, exponent, p)
    
    # The result will be 1 if it's a residue,
    # and p-1 (which is -1 mod p) if it's a non-residue.
    return legendre_symbol == 1
a = 5
p = 10

if is_quadratic_residue(a, p):
    print(f"{a} is a quadratic residue modulo {p}")
else:
    print(f"{a} is NOT a quadratic residue modulo {p}")
