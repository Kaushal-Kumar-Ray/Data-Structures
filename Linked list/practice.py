class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def add_at_head(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
ll=LinkedList()
ll.add_at_head(10)
ll.add_at_head(13)
ll.add_at_head(20)
ll.print_list()            
                        