n=int(input())
while n>0:
    rem=n%10
    n1=0
    n1=(n1*10)+rem
    n=n//10
if n==n1:
    print("the no is palindrom")
else:
    print("no")