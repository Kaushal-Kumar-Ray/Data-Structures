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
        
    def add_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:  # Stop at the last node
            temp = temp.next
        temp.next = new_node
        
    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None



    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print(None)
        
ll = LinkedList()
ll.add_at_head(3)
ll.add_at_head(2)
ll.add_at_head(1)
ll.add_at_end(4)
ll.print()  # Output: 1->2->3->4->None
ll.delete_node(3)
ll.print()  # Output: 1->2->4->None