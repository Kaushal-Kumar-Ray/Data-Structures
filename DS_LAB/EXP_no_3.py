class Node:
    def __init__(self, data,next=None):
        self.data=data
        self.next=next
class LL:
    def __init__(self):  
        self.head=None
    def insert_at_beginning(self,node):
        node.next=self.head
        self.head=node
    def insert_at_last(self,node):                   
        temp=self.head
        if temp:
            while temp.next != None:
                temp=temp.next
            temp.next=node
        else:
            self.insert_at_beginning(node)
    def display(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data)
                temp=temp.next
    def insert_after(self,num,node):
        p=self.head
        if not p:
            self.insert_at_beginning(node)
        else:
            while p!=None and p.data!=num:
                p=p.next
            if p:
                node.next=p.next
                p.next=node
            else:
                print("No such data found")
    def del_at_beginning(self):
        t=self.head
        if t:
            self.head=self.head.next
            del t
    def del_at_last(self):
        p=None
        t=self.head
        if t:
            while t.next != None:
                p=t
                t=t.next
            p.next=None
            del t
            print("successfully deleted")
    def del_num(self,num):
        p=None
        t=self.head
        if t.data==num:
            self.head=t.next
            del t
        elif t:
            while t!=None and t.data!=num:
                p=t
                t=t.next
            if t==None:
                print("data not found")
            else:
                p.next=t.next
                del t
                print("Successfully deleted")
               
ll=LL()
while 1:
    print("Press 1 to insert at beginning")
    print("Press 2 to insert at last")
    print("press 3 to insert after specific data")
    print("press 4 to delete at beginning")
    print("press 5 to delete at last")
    print("press 6 to delete particulat data")
    print("press 7 to display")
    print("press 8 to exit")
    
    choice=int(input(""))
    if choice>0 and choice<4:
        data=int(input("Enter the number"))
        node=Node(data)
        if choice == 1:
            ll.insert_at_beginning(node)
        elif choice==2:
            ll.insert_at_last(node)
        else:
            num=int(input("Enter the number after which you have to insert"))
            ll.insert_after(num,node)
    elif choice >3 and choice<7:
        if choice==4:
            ll.del_at_beginning()
        elif choice==5:
            ll.del_at_last()
        else:
            num=int(input("Enter the number which you want to delete"))
            ll.del_num(num)
    elif choice==7:
        ll.display()
    elif choice==8:
        print("Exiting the program")
        break
    else:
        print("Invalid choice, please try again")
        
       
