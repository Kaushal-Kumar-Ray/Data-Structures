class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def inorder(root):
    if root:
        inorder(root.leftchild)
        print(root.data, end=" ")
        inorder(root.rightchild)

# Creating the tree
root = TreeNode('N1')
root.leftchild = TreeNode('N2')
root.rightchild = TreeNode('N3')
root.leftchild.leftchild = TreeNode('N4')
root.leftchild.rightchild = TreeNode('N5')

# In-order traversal
print("In order traversal in tree")
inorder(root)