def digital_root(n):
    while n >= 10:          
        s = 0
        while n > 0:
            s += n % 10     
            n //= 10       
        n = s               
    return n                
n=15
print(digital_root(n))