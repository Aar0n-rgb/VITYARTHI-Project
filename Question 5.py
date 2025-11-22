def is_abundant(n):
    if n < 1:
        return False
    
    sum_divisors = 1 
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_divisors += i
            if i != n // i:  
                sum_divisors += n // i
        i += 1
    return sum_divisors > n
n=23
print(is_abundant(n))