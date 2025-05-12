class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse linked list in groups of size k
def reverse_in_groups(head, k):
    current = head
    prev = None
    next = None
    count = 0

    # Reverse first k nodes of the linked list
    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    # next is now a pointer to (k+1)th node
    if next is not None:
        head.next = reverse_in_groups(next, k)

    # prev is now the new head of the reversed group
    return prev

# Function to insert a new node at the end
def append(head, data):
    if head is None:
        return Node(data)
    else:
        current = head
        while current.next:
            current = current.next
        current.next = Node(data)
        return head

# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()

# Main Program
if __name__ == "__main__":
    head = None
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3  # Group size

    for item in elements:
        head = append(head, item)

    print("Original Linked List:")
    print_list(head)

    head = reverse_in_groups(head, k)

    print(f"Reversed in groups of size {k}:")
    print_list(head)