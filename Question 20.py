base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
modulus = int(input("Enter modulus: "))

result = 1
for i in range(exponent):
    result = (result * base) % modulus

print("Result:", result)
