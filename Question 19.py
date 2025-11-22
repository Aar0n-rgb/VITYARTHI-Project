n = int(input("Enter a number: "))

def count_divisors(x):
    c = 0
    for i in range(1, x + 1):
        if x % i == 0:
            c += 1
    return c

is_highly_composite = True

for i in range(1, n):
    if count_divisors(i) >= count_divisors(n):
        is_highly_composite = False
        break

if is_highly_composite:
    print(f"{n} is a Highly Composite Number")
else:
    print(f"{n} is NOT a Highly Composite Number")
