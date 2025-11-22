def is_pronic(n):
    for i in range(n+1):     
        if i * (i+1) == n:     
            return True
    return False
n=20
print(is_pronic(n))