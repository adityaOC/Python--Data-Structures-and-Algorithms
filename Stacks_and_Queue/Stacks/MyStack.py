"""

This file contains stack implementation with python list



    Stack() 
    push(item) 
    pop() 
    peek()
    isEmpty() 
    size() 
    displayAllElements()


"""


class MyStack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items)< 1 :
            return None
        else:
            return self.items[len(self.items)-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def displayAllElements(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.items)
    def displayAllElementsInReverseOrder(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            temp = []
            i = len(self.items)-1
            while i != -1:
                temp.append(self.items[i])
                i -= 1

            print(temp)


"""
stack = MyStack()
stack.push(5)
stack.push(6)
stack.push(50)
stack.displayAllElements()
print(stack.peek())
stack.pop()
stack.displayAllElements()
print(stack.size())
"""
