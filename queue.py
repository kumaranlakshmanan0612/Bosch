class Queue:
    def __init__(self):
        self.data = []
        self.head = 0  # index of current front
 
    def enqueue(self, item):
        self.data.append(item)
 
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.data[self.head]
        self.head += 1
        # Periodically trim the list to avoid unbounded growth
        if self.head > 32 and self.head > len(self.data) // 2:
            self.data = self.data[self.head:]
            self.head = 0
        return item
 
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.data[self.head]
 
    def is_empty(self):
        return self.head >= len(self.data)
 
    def size(self):
        return len(self.data) - self.head
    

def main():
    q1=Queue()
    q1.enqueue(2)
    print(q1.peek())

if __name__=="__main__":
    main()