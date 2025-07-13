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
def postorder_traversal(root):
     if root is None:
          return
     postorder_traversal(root.left)
     postorder_traversal(root.right)
     print(root.data,end=" ")
def no_of_node(root):
     c=1
     if root is not None:
          return c+no_of_node(root.left)+no_of_node(root.right)
     else:
          return 0

          
     
arr=[1,2,-1,-1,3,4,-1,-1,5,-1,-1]
root=build_tree(arr)

print(no_of_node(root))
# print(root.data)

# postorder_traversal(root)        