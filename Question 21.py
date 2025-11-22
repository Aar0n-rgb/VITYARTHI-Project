def extended_gcd(a, b):
    
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    """
    Finds the modular multiplicative inverse x such that (a * x) % m = 1.
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        # The modular inverse does not exist
        return None
    else:
        # x may be negative, so we wrap it to be in the range [0, m-1]
        return x % m
a = 3
m = 11

inv = mod_inverse(a, m)
if inv is None:
    print("Modular inverse does not exist")
else:
    print(f"Modular inverse of {a} modulo {m} is {inv}")
