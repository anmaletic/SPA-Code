class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):        
        a = self.head
        s = ''
        while a != None:
            s += str(a) + ' -> '
            a = a.next
        return s[:-4]
    
    def add(self, v):
        a = Node(v)
        if self.head == None:
            self.head = a
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = a

    def delete(self, v):
        while self.head.value == v:
            self.head  = self.head.next
        a = self.head
        b = self.head.next
        while b != None:
            if b.value == v:
                a.next = b.next
            a = b
            b = b.next

    def __iter__(self):
        self.tmp = self.head
        return self

    def __next__(self):
        if self.tmp != None:
            x = self.tmp.value
            self.tmp = self.tmp.next
            return x
        else:
            raise StopIteration

class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, v):
        t = Node(v)
        t.next = self.head
        self.head = t

    def pop(self):
        if self.isEmpty():
            raise IndexError('Lista je prazna')
        else:
            t = self.head.value
            self.head = self.head.next
            return t

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        return self.head == None

    
class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = self.head

    def enqueue(self, v):
        t = Node(v)
        if self.head == None:
            self.head = t
            self.tail = t
        else:
            self.tail.next = t
            self.tail = t
            
    def isEmpty(self):
        return self.head == None

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Red je prazan')
        else:
            t = self.head.value
            self.head = self.head.next
            return t
    
        


    
