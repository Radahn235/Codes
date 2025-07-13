class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Diameter:
    def __init__(self):
        self.diameter = 0  # initialize instance variable

    def height(self, node):
        if node is None:
            return 0
        # Use self.height instead of undefined height()
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        # Update self.diameter
        self.diameter = max(self.diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

# Build tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

# Create object and call
d = Diameter()
d.height(root)
print("Diameter of Binary Tree:", d.diameter)
