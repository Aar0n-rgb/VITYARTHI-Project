def is_deficient(n):
    return sum(i for i in range(1, n) if n % i == 0) < n
n=6
print(is_deficient(n))