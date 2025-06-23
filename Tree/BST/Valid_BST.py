class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.data < max_val):
        return False
    return (is_valid_bst(root.left, min_val, root.data) and 
            is_valid_bst(root.right, root.data, max_val))

# Example usage:
if __name__ == "__main__":
    # Constructing a valid BST
    #       10
    #      /  \
    #     5   15
    #        /  \
    #       12   20

    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(12)
    root.left.right = Node(20)

    print("Is valid BST:", is_valid_bst(root))  # Output: True
