a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum_a = 0
for i in range(1, a):
        if a % i == 0:
            sum_a += i
            sum_b = 0
for i in range(1, b):
            if b % i == 0:
                sum_b += i
if sum_a == b and sum_b == a:
        print("Amicable numbers")
else:
    print("Not amicable numbers")