def numto0(n):
    count=0
    if n==0:
        return 0
    else:
        count+=1
        return count+numto0(n-1)
print(numto0(5))