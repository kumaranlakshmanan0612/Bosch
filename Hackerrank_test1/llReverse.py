class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def print_reverse(self,node):
        if node:
            self.print_reverse(node.next)
            print(node.data,end=" ")

ll = LinkedList()
ll.append(4)
ll.append(5)
ll.append(6)
ll.print_reverse(ll.head)