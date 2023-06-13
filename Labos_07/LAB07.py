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
    
        
class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def preorder(self):
        s = str(self.value)
        if self.left != None:
            s += self.left.preorder()
        if self.right != None:
            s += self.right.preorder()
        return s

    def inorder(self):
        s = ''
        if self.left != None:
            s += self.left.inorder()
        s += str(self.value)
        if self.right != None:
            s += self.right.inorder()
        return s

    def postorder(self):
        s = ''
        if self.left != None:
            s += self.left.postorder()
        if self.right != None:
            s += self.right.postorder()
        s += str(self.value)
        return s   
        
    def bst(self, a):
        r = Tree(a[0])
        for i in range(1, len(a)):
            t = Tree(a[i])
            done = False
            tmp = r
            while not done:
                if tmp.value >= t.value:
                    if tmp.left == None:
                        tmp.left = t
                        done = True
                    else:
                        tmp = tmp.left
                else:
                    if tmp.right == None:
                        tmp.right = t
                        done = True
                    else:
                        tmp = tmp.right
        return r


class Heap:
    def __init__(self):
        self.data = []
        self.size = 0

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, v):
        self.data.append(v)
        self.size += 1
        done = False
        i = self.size - 1
        i = len(self.data) - 1
        while not done:
            p = self.parent(i)
            if p >= 0 and self.data[p] > self.data[i]:
                self.data[p], self.data[i] = self.data[i], self.data[p]
                i = p
            else:
                done = True
    
            
    def heapify(self, i):        
        done = False
        while not done:
            mini = i
            left = self.left(i)
            right = self.right(i)
            if left < self.size and self.data[left] < self.data[mini]:
                mini = left
            if right < self.size and self.data[right] < self.data[mini]:
                mini = right                
            if mini != i:
                self.data[i], self.data[mini] = self.data[mini], self.data[i]
                i = mini
            else:
                done = True

    def buildHeap(self, a):
        self.data = a
        self.size = len(a)
        for i in range(self.size // 2, -1, -1):
            self.heapify(i)

    def remove(self):        
        if self.size > 1:
            t = self.data[0]
            self.data[0] = self.data.pop()
            self.size -= 1
            self.heapify(0)
            return t
        elif self.size == 1:
            self.size = 0
            return self.data.pop()
        else:
            raise Exception('Hrpa je prazna')

