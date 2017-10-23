class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def displayAllElements(self):
        if self.isEmpty():
            print("Deque is empty")
        else:
            print(self.items)


deque = Deque()

deque.addFront(5)
deque.addRear(42)
deque.addRear(12)
print(deque.size())
deque.displayAllElements()
deque.removeFront()
deque.removeRear()
deque.displayAllElements()