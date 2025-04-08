class Node:
    def __init__(self, data):
        self.data = data  # Store person's position
        self.next = None  # Pointer to next person


class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initially empty

    def append(self, data):
        """Add a person to the circular linked list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # Circular link to itself
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # Circular connection

    def josephus(self, k):
        """Solves the Josephus problem"""
        temp = self.head

        # Only one person remains
        while temp.next != temp:
            for _ in range(k - 1):  # Move k-1 steps
                temp = temp.next

            print(f"Eliminating: {temp.next.data}")  # Remove next person
            temp.next = temp.next.next  # Skip eliminated person

        return temp.data  # Last remaining person
    
# **Example:**
cll = CircularLinkedList()
for i in range(1, 8):  # 7 peopl
    cll.append(i)

survivor = cll.josephus(3)  # k = 3 (every 3rd person eliminated)
print(f"The survivor is at position: {survivor}")
