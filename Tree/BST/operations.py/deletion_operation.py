class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insertion in BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Find minimum value node
def find_min(node):
    while node.left:
        node = node.left
    return node

# Deletion in BST
def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Node with one or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
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

print("In-order before deletion:")
inorder(root)

root = delete(root, 10)

print("\nIn-order after deleting 10:")
inorder(root)

