from Stacks_and_Queue.Queues.MyQueue import MyQueue


class StackWithQ:

    def __init__(self):
        self.q = MyQueue()


    def push(self,ele):
        self.q.enqueue(ele)

    def pop(self):
        size = self.q.size()
        if size == 0:
            print("stack empty")
        else:

            for i in range(1,size):
                temp = self.q.dequeue()
                self.q.enqueue(temp)

            return self.q.dequeue()

stack = StackWithQ()
stack.push("A")
stack.push("B")
stack.push("C")
print(stack.pop())



