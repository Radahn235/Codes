a = input("Enter the string: ")
a = list(a)  # Convert string to list for swapping
i = 0
j = len(a) - 1

while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

reversed_a = ''.join(a)  # Convert list back to string
print("Reversed string:", reversed_a)
