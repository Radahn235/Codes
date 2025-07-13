#1
numbers=[1,2,3,4,5]
total=0
for num in numbers:
    total+=num    
print("sum:",total)
#2
numbers1=5
factorial=1
while numbers1 >0:
    factorial*=numbers1
    numbers1-=1   
print("factorial:",factorial)
#3
for i in range(1,6):
    for j in range(1,11):
        print(i*j,end="\t")
    print()
#4
for i in range(1,10,2):
    print(i)
#5
for ch in 'vs_code':
    print(ch,end='\t')
#6
m=[(1,2,3),
   (4,5,6),
   (7,8,9)]
for i in range(3):
    for j in range(3):
        print(m[i][j],end='\t')
    print()
sum=0
for i in range(3):
    for j in range(3):
        sum+=m[i][j]
print("Sum is:",sum)
#7
m=[(1,2,3),
   (4,5,6),
   (7,8,9)]
for row in m:
    print(row)
        