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
    

    def remove_nth_node_from_back(self,N):
        slow=self.head
        fast=self.head
        for _ in range(N):
            fast=fast.next
        
        while fast.next:
            slow=slow.next
            fast=fast.next
        removed=slow.next
        slow.next=slow.next.next
        removed=None

ll=Linkedlist()
ll.insert_at_beginning(50)
ll.insert_at_beginning(40)
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)

ll.print_ll()
ll.remove_nth_node_from_back(2)
ll.print_ll()