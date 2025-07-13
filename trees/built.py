class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def build_tree(root):
    if root is None:
        return
    print(root.data,end=" ")
    build_tree(root.left)#will build left side
    build_tree(root.right)#will build right side
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
build_tree(root)
        