def selsort(a):
    min=0
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    return a
a=[5,8,1,6,2]
print(selsort(a))

