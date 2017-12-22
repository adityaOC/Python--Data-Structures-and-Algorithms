

class SinglyListNode():

    def __init__(self,value):
        self.value = value
        self.nextnode = None


class LinkedList():

    def __init__(self,value):
        newNode = SinglyListNode(value)
        self.head = newNode
        self.tail = newNode
        self.size = 1



    def appendNode(self,value):

        newNode = SinglyListNode(value)

        self.tail.nextnode = newNode
        self.tail = newNode
        self.size += 1

    def insertAfterNode(self,value,index):

        if index<1 or index > self.size:
            print("Invalid index value")
            return
        elif index == self.size:
                self.appendNode(value)

                return
        else:

            i= 1
            node = self.head
            while i<index:
                node = node.nextnode
                i += 1

            newNode = SinglyListNode(value)
            temp = node.nextnode
            node.nextnode = newNode
            newNode.nextnode = temp
            self.size +=1





    def traverseList(self):

        node = self.head
        while node != None:
            print(node.value)
            node = node.nextnode




list = LinkedList(10)
list.appendNode(20)
list.appendNode(30)

#list.traverseList()

list.insertAfterNode(15,3)
list.appendNode(40)
list.insertAfterNode(50,5)



list.traverseList()








