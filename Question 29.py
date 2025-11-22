def polygonal_number(s, n):
    return ((s - 2) * n * n - (s - 4) * n) // 2
# Triangle numbers (s=3)
for i in range(1, 6):
    print(polygonal_number(3, i), end=" ")
