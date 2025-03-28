class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_at_head(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next  # Corrected variable name
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print(None)
        
ll = LinkedList()
ll.add_at_head(30)
ll.add_at_head(20)
ll.add_at_head(10)

print("Original List:")
ll.print()

# Reverse the linked list
print("Reversed List:")
ll.reverse()
ll.print()