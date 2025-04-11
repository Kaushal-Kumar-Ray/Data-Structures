from collections import deque  # Corrected 'form' to 'from'

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

# preorder operation
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.leftchild)
        preorder(root.rightchild)

# postorder operation
def postorder(root):
    if root:
        postorder(root.leftchild)
        postorder(root.rightchild)        
        print(root.data, end=" ")

# inorder operation
def inorder(root):
    if root:
        inorder(root.leftchild)
        print(root.data, end=" ")
        inorder(root.rightchild)    
            
# level order operation
def levelorder(root):
    if not root:
        return
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        print(current.data, end=" ")
        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)

# Function to print the tree structure
def print_tree(node, level=0, prefix="Root: "):  # Renamed to 'print_tree'
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.data))
        print_tree(node.leftchild, level + 1, "L--- ")
        print_tree(node.rightchild, level + 1, "R--- ")

# Example usage: Creating a binary tree
root = TreeNode('N1')
root.leftchild = TreeNode("N2")
root.rightchild = TreeNode("N3")

root.leftchild.leftchild = TreeNode("N4")
root.leftchild.rightchild = TreeNode("N5")
root.rightchild.leftchild = TreeNode("N6")
root.rightchild.rightchild = TreeNode("N7")
root.leftchild.leftchild.leftchild = TreeNode("N8")
root.leftchild.leftchild.rightchild = TreeNode("N9")
root.rightchild.leftchild.leftchild = TreeNode("N10")
root.rightchild.leftchild.rightchild = TreeNode("N11")
root.rightchild.rightchild.leftchild = TreeNode("N12")
root.rightchild.rightchild.rightchild = TreeNode("N13")
root.leftchild.leftchild.leftchild.leftchild = TreeNode("N14")
# Calling the traversal functions
print("Pre order traversal")
preorder(root)

print("\nPost order traversal")
postorder(root)

print("\nIn order traversal")
inorder(root)

print("\nLevel order traversal")
levelorder(root)

# Calling the print_tree function to display the tree structure
print("\nTree Structure:")
print_tree(root)