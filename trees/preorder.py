class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def build_tree(arr):
    index=-1
    def build():
        nonlocal index
        index+=1
        if index>=len(arr):
            return None
        if arr[index]==-1:
                return None
        node=Node(arr[index])
        node.left=build()
        node.right=build()
        return node
    return build()
def preorder_traversal(root):
     if root is None:
          return
     print(root.data,end=" ")
     preorder_traversal(root.left)
     preorder_traversal(root.right)
arr=[1,2,-1,-1,3,4,-1,-1,5,-1,-1]
root=build_tree(arr)
# print(root.data)
preorder_traversal(root)        