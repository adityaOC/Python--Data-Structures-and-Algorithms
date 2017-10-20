

class BinaryHeap():

    def __init__(self):
        self.list = [0]
        self.count = 0

    def display(self):
        print(self.list)



    def percUP(self,i):

        while i // 2 > 0:
            if self.list[i] < self.list[i // 2]:
                #self.swap(self.list[i],self.list[i // 2])
                temp = self.list[i]
                self.list[i] = self.list[i // 2]
                self.list[i // 2] = temp

            i = i // 2


    def insert(self,key):

        self.list.append(key)
        self.count = self.count + 1
        self.percUP(self.count)

    def getMinChild(self,i):
        if self.list[ i * 2] < self.list[(i*2)+1]:
            return (i*2)
        else:
            return (i*2) + 1


    def percDown(self,i):

        minChildIndex = self.getMinChild(i)
        while (i *2)<= self.count:

            if self.list[i] > self.list[minChildIndex]:
                temp = self.list[i]
                self.list[i] = self.list[minChildIndex]
                self.list[minChildIndex] = temp

            i = minChildIndex


    def deleMin(self):

        print("deleted : {}".format(self.list[1]))
        self.list[1] = self.list[self.count]
        self.list.pop()

        self.count = self.count - 1
        self.percDown(1)




heap = BinaryHeap()
heap.insert(10)
heap.display()
heap.insert(20)
heap.display()
heap.insert(5)
heap.display()
heap.insert(40)
heap.display()
heap.insert(15)
heap.display()
heap.insert(50)
heap.display()

heap.deleMin()
heap.display()

