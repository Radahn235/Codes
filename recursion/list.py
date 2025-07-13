#1
my_list=[10,20,30,40,50]
print(my_list[1:4])
print(my_list[0:5:2])
print(my_list[::-1])
#2
squares=[x for x in range(1,11) if x%2==0 ]
print(squares)
#3
chars=[char.upper() for char in "python"]
print(chars)
#4(
pairs=[(x,y) for x in range(1,4) for y in range(4,7) ]
print(pairs)
#5
matrix=[[1,2],[3,4],[5,6]]
flattened=[num for row in matrix for num in row]
print(flattened)
#6
labels=["even" if x%2==0 else "odd" for x in range(1,6)]
print(labels)
#7
def square(x):
    return x*x
sq=[sq(x)for x in range(1,5)]
print(sq)
