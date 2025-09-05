class Stack:
    def __init__(self):
        self.arr=[]
 
    def push(self, item):
        self.arr.append(item)
 
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.arr.pop()
 
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.arr[-1]
 
    def is_empty(self):
        return len(self.arr) == 0
 
    def size(self):
        return len(self.arr)

def main():
    s1=Stack()
    s1.push(0)
    s1.push(1)
    s1.push(3)
    print(s1.pop())
    print(s1.peek())
    print(s1.is_empty())

if __name__ == "__main__":
    main()
    