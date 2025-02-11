class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,value):
        node=Node(value)
        node.next=self.head
        self.head=node
    
    def print_ll(self):
        temp=self.head
        while temp:
            print(temp.value,end="->")
            temp=temp.next
        
        print("None")
    
    def reverse(self):
        current=self.head
        prev=None
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

ll=Linkedlist()
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)

ll.print_ll()
ll.reverse()
ll.print_ll()        
