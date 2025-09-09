class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()