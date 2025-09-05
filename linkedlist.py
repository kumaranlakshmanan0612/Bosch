class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self._size=0

    def add(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=node
        self._size+=1

    def prepend(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
        self._size+=1

    def delete(self,data):
        prev,curr=None,self.head
        while curr:
            if curr.data==data:
                if prev is None:
                    self.head=curr.next
                else:
                    prev.next=curr.next
                self._size-=1
                return True
            prev,curr=curr,curr.next
        return False

    def display(self):
        vals=[]
        curr=self.head
        while curr:
            vals.append(str(curr.data))
            curr=curr.next
        s=" -> ".join(vals) if vals else "<empty>"
        print(s)
        return s

    def __len__(self):
        return self._size

    def __iter__(self):
        return iter(self.to_list())

    def to_list(self):
        vals=[]
        curr=self.head
        while curr:
            vals.append(curr.data)
            curr=curr.next
        return vals


if __name__=="__main__":
    sll=SinglyLinkedList()
    sll.add(10)
    sll.add(20)
    sll.add(30)
    sll.display()
    sll.prepend(5)
    sll.display()
    sll.delete(20)
    sll.display()
    print(len(sll))
    for item in sll:
        print(item,end=" ")
