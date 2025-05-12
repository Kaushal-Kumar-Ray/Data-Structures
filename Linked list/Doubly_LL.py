class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
         self.head = None
         
    def add_at_head(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
            
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
 # Example Usage
dll = DoublyLinkedList()
dll.add_at_head(30)
dll.add_at_head(20)
dll.add_at_head(10)
dll.print_list()







'''FOR TAIL ADDITION'''
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
         
    def add_at_head(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def add_at_tail(self, new_data):
        new_node = Node(new_data)
        if not self.head:  # If list is empty, new node becomes the head
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node  # Link last node to new node
        new_node.prev = temp  # Link new node to last node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example Usage
dll = DoublyLinkedList()
dll.add_at_head(20)
dll.add_at_head(10)
dll.add_at_tail(30)
dll.add_at_tail(40)
dll.print_list()  
'''