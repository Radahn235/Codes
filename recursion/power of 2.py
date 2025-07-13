def powerof2(n):
    count=0
    if n==1:
        return True
    if n%2!=0 or n==0:
        return False
    else:
        return powerof2(n//2)

res=powerof2(3)
print(res)

