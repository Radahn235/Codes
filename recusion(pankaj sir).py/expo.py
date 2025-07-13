def expo(n,m):
    if m==0:
        return 1
    return n*expo(n,m-1)
   
res=expo(3,3)
print(res)