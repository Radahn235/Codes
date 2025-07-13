arr=[1,2,3,4,5,6,7,8]
var=0
num=int(input("enter the num:"))
for i in range(len(arr)):
    if num==arr[i]:
        print("num is present")
        var+=1
        break
if var==0:
    print("num is not present")