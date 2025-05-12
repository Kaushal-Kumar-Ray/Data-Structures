class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function for inorder traversal without recursion
def inorder_traversal(root):
    stack = []
    current = root

    while True:
        # Reach the leftmost node of the current node
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break

# Function to create a simple binary tree for demonstration
def build_sample_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(11)
    root.left.right = Node(9)

    return root

# Main Program
if __name__ == "__main__":
    root = build_sample_tree()
    print("Inorder Traversal (Without Recursion):")
    inorder_traversal(root)