def count0(n):
    if n == 0:
        return 0
    if n % 10 == 0:
        return 1 + count0(n // 10)
    else:
        return count0(n // 10)

print(count0(10))  
