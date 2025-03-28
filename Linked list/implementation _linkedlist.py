class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node (Initially None)

class LinkedList:  # Correct indentation (outside Node class)
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Add new node at the head
    def add_at_head(self, new_data):
        new_node = Node(new_data)  # Create a new node
        new_node.next = self.head  # Point new node to the current head
        self.head = new_node  # Update head to the new node

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

# Create an empty linked list
ll = LinkedList()

# Add nodes at the head
ll.add_at_head(30)
ll.add_at_head(20)
ll.add_at_head(10)

# Print the linked list
ll.print_list()
