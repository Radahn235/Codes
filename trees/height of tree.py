class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def solve(node):
        if node==None:
            return 0
        left_height=solve(node.left)
        right_height=solve(node.right)
        return 1+max(left_height,right_height)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.right=Node(8)
print(solve(root))