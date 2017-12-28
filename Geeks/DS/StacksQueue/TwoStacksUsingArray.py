


class TwoStacks:

    def __init__(self,arraySize):
        self.arraySize = arraySize
        self.array = [None]*self.arraySize
        self.stack1Top = -1
        self.stack2Top = self.arraySize

    def stack1Push(self,ele):

        if self.stack1Top<self.stack2Top-1:
            self.stack1Top += 1
            self.array[self.stack1Top] = ele

        else:
            print("overflow")
            return None


    def stack2Push(self,ele):

        if self.stack1Top<self.stack2Top-1:

            self.stack2Top -= 1
            self.array[self.stack2Top] = ele
        else:

            print("overflow")
            return


    def stack1Pop(self):

        if self.stack1Top< 0:
            print("stack empt")
            return None
        else:
            ele = self.array[self.stack1Top]
            self.array[self.stack1Top] = None
            self.stack1Top -=1
            return ele

    def stack2Pop(self):

        if self.stack2Top > self.arraySize-1:
            print("stack empt")
            return None
        else:
            ele = self.array[self.stack2Top]
            self.array[self.stack2Top] = None
            self.stack2Top += 1
            return ele


stack = TwoStacks(6)
stack.stack1Push(10)
stack.stack1Push(20)
stack.stack1Push(30)
#stack.stack1Push(40)




stack.stack2Push("A")
stack.stack2Push("B")
stack.stack2Push("C")
stack.stack2Push("D")

print(stack.stack2Pop())
print(stack.stack2Pop())

print(stack.stack1Pop())
print(stack.stack1Pop())







