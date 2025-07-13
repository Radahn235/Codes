rows = 5

# Top Half
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# Bottom Half (Start from rows - 1 to avoid repeating middle row)
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
