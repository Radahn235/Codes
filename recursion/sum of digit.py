def sumofdigit(n):
    if n==0:
        return 0
    else:
        return n%10+sumofdigit(n//10)
res=sumofdigit(1234)
print(res)