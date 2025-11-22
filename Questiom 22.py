def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        # Inverse doesn't exist
        return None
    else:
        return x % m

def crt(remainders, moduli):
    if len(remainders) != len(moduli):
        raise ValueError("Input lists must have the same length")

    N = 1
    for m in moduli:
        N *= m

    total = 0
    for i in range(len(moduli)):
        r_i = remainders[i]
        m_i = moduli[i]
        
        # N_i = N / m_i
        N_i = N // m_i
        
        # Find the modular inverse of N_i modulo m_i
        y_i = mod_inverse(N_i, m_i)
        
        if y_i is None:
            raise ValueError("Moduli are not pairwise coprime, inverse not found.")

        total += r_i * N_i * y_i

    # The final solution is total % N
    return total % N
remainders = [2, 3, 2]
moduli = [3, 5, 7]

x = crt(remainders, moduli)
print(f"The solution x is: {x}")
