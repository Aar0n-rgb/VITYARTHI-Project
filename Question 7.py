def is_harshad(n):
    s = sum(int(d) for d in str(n))
    return n % s == 0
n=58
print(is_harshad(n))