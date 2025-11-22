def is_automorphic(n):
    return str(n*n).endswith(str(n))
n=24
print(is_automorphic(n))