n = int(input("Enter a number: "))
count = 0

while n >= 10:
    product = 1
    for digit in str(n):
        product *= int(digit)
    n = product
    count += 1

print("Multiplicative persistence:", count)
