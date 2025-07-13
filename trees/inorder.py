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
def inorder_traversal(root):
     if root is None:
          return
     inorder_traversal(root.left)
     print(root.data,end=" ")
     inorder_traversal(root.right)
arr=[1,2,3,-1,-1,-1,4,-1,5,6,-1,-1]
root=build_tree(arr)
# print(root.data)
inorder_traversal(root)        