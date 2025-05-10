class Node:
    def __init__(self, key):
        self.key = key; self.left = self.right = None; self.height = 1

def height(n): return n.height if n else 0
def balance(n): return height(n.left) - height(n.right) if n else 0

def rotate_right(y):
    x, T2 = y.left, y.left.right
    x.right, y.left = y, T2
    y.height, x.height = 1 + max(height(y.left), height(y.right)), 1 + max(height(x.left), height(x.right))
    return x

def rotate_left(x):
    y, T2 = x.right, x.right.left
    y.left, x.right = x, T2
    x.height, y.height = 1 + max(height(x.left), height(x.right)), 1 + max(height(y.left), height(y.right))
    return y

def insert(root, key):
    if not root: return Node(key)
    if key < root.key: root.left = insert(root.left, key)
    else: root.right = insert(root.right, key)
    
    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)
    
    if b > 1 and key < root.left.key: return rotate_right(root)
    if b < -1 and key > root.right.key: return rotate_left(root)
    if b > 1 and key > root.left.key: root.left = rotate_left(root.left); return rotate_right(root)
    if b < -1 and key < root.right.key: root.right = rotate_right(root.right); return rotate_left(root)
    
    return root

def pre_order(n):
    if n:
        print(n.key, end=' ')
        pre_order(n.left)
        pre_order(n.right)

# Example
root = None
for k in [10, 20, 30, 40, 50, 25]:
    root = insert(root, k)
pre_order(root)
