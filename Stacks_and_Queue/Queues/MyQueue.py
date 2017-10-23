"""

This file contains Queue implementation with python list



    Queue() 
    enqueue(item) 
    dequeue()  
    size()() 
    isEmpty() 
    displayAllElements()


"""


class MyQueue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def displayAllElements(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.items)
"""
queue = MyQueue()
queue.displayAllElements()
queue.enqueue(5)
queue.enqueue(12)
queue.enqueue(32)
queue.displayAllElements()
queue.dequeue()
queue.displayAllElements()
"""