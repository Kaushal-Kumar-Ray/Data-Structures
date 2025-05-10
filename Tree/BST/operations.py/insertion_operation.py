class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insertion in BST
def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# In-order traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# Example usage
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 20)
root = insert(root, 15)

print("In-order insertion:")
inorder(root)


