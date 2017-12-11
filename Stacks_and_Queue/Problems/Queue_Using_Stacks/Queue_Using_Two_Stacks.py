from Stacks_and_Queue.Stacks.MyStack import MyStack

class queue():

    def __init__(self):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        #self.stack1.push(ele)
        self.currentStack = self.stack1

    def enqueue(self,ele):
        if self.currentStack == self.stack1:

            self.stack1.push(ele)
        else:
            while not self.stack2.isEmpty():
                self.stack1.push(self.stack2.pop())
            self.currentStack = self.stack1
            self.stack1.push(ele)
        self.displayAllElement()

    def dequeue(self):

        if self.currentStack == self.stack2:
            self.stack2.pop()
        else:
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())

            self.currentStack = self.stack2
            self.stack2.pop()
        self.displayAllElement()

    def getSize(self):

        return self.currentStack.size()

    def displayAllElement(self):

        if self.currentStack == self.stack1:
            self.stack1.displayAllElements()
        else:
            self.stack2.displayAllElementsInReverseOrder()




q = queue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.dequeue()
q.dequeue()

q.enqueue(50)

q.dequeue()










