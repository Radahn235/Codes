from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def level(node):
    res=[]
    queue=deque()
    queue.append(node)
    while len(queue)!=0:
        e=queue.left.pop()
        res.append(e.data)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return res

root=Node(1)
root.left=Node(2)
root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)

res=level(root)
print(res)
        