class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list

    # Add node at head
    def add_at_head(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Reverse the linked list (Iterative method)
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next  # Store next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev forward
            curr = next_node  # Move curr forward
        self.head = prev  # Update head to the new first node

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

# Create linked list
ll = LinkedList()
ll.add_at_head(30)
ll.add_at_head(20)
ll.add_at_head(10)

print("Original List:")
ll.print_list()

# Reverse the linked list
print("Reversed List:")
ll.reverse()
ll.print_list()
