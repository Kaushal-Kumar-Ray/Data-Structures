class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
   
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        
    def print_list(self):
        temp = self.head
        if self.head:
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
            print("self.head.data")  # To show the circular nature
 # Example Usage
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.print() 