#1
a=[7,18,45,8,10,49]
t=0
for i in range(len(a)):
    for j in range (len(a)-i-1):
         if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("sorted array:",a)

#2
a=[7,18,45,8,10,49]
t=0
for i in range(len(a)):
    for j in range (len(a)-i-1):
         if a[j]>a[j+1]: 
             a[j],a[j+1]=a[j+1],a[j]
                    
print("sorted array:",a)





