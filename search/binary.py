a=[10,20,40,50,15,25,30]
a.sort()
print("sorted array",a)
t=int(input("enter the target:"))
s=0
e=len(a)-1
while(s<=e):
    m=(s+e)//2
    if a[m]==t:
        print("element found at index",m)
        break
    if a[m]<t:
        s=m+1
    if a[m]>t:
        e=m-1
else:
        print("element not found")
