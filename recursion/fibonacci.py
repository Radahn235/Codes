def fibonacci(n):
    if n<=1: #base case: return n if its 0 or 1
        return n
    else: #recursive case: sum of previous two fibonacci numbers
        return fibonacci(n-1)+fibonacci(n-2)
result=fibonacci(6)
print(result)