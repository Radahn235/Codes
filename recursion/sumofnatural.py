def sumofnat(n):
    if n==0:
        return 0
    else:
        return n+ sumofnat(n-1)
result=sumofnat(5)
print(result)