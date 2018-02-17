"""Delete all nodes with duplicate values from sorted linked list"""



class LinkedList:

    def __init__(self,value):
        self.value = value
        self.nextNode = None


def deleteDuplicates(node):


    adjecentNode = node.nextNode


    while node and adjecentNode:

        if node.value == adjecentNode.value:
            node.nextNode = adjecentNode.nextNode
            adjecentNode = node.nextNode
        else:

            node = node.nextNode
            adjecentNode = node.nextNode


def display(node):

    while node:
        print(node.value)
        node = node.nextNode



a = LinkedList(1)
a.nextNode = LinkedList(2)
a.nextNode.nextNode = LinkedList(3)
a.nextNode.nextNode.nextNode =  LinkedList(3)
a.nextNode.nextNode.nextNode.nextNode =  LinkedList(3)
a.nextNode.nextNode.nextNode.nextNode.nextNode = LinkedList(4)
a.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode = LinkedList(5)


deleteDuplicates(a)


display(a)