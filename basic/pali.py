n=int(input("enter the num:"))
org=n
rev=0
while n>0:
    res=n%10
    
    rev=(rev*10)+res
    n=n//10
if org==rev:
    print("no. is pali")
else:
    print("not") 