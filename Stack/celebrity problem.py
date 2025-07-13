class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.top = None

    def traversal(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next
        print("end of Stack")

    def pop(self):
        if self.top is None:
            return -1
        data = self.top.data
        self.top = self.top.next
        return data  # ← return data

    def push(self, value):
        if self.size() >= self.maxsize:
            print("stack overflow") 
            return
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def size(self):
        temp = self.top
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count


def find_celeb(mat, n):
    stack = Stack(n)
    for i in range(n):
        stack.push(i)

    while stack.size() >= 2:
        i = stack.pop()
        j = stack.pop()
        if mat[i][j] == 0:
            stack.push(i)
        else:
            stack.push(j)

    celeb = stack.pop()

    for i in range(n):
        if i != celeb:
            if mat[i][celeb] != 1 or mat[celeb][i] != 0:
                return -1
    return celeb


# Test matrix
mat = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]

print("Celebrity is:", find_celeb(mat, 4))
