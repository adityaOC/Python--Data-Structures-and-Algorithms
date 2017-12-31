

from Linked_Lists.SinglyLinkedList import SinglyListNode


def getUnion(startNode_List1,startNode_List2):

    hashTable = {}
    currentNode = startNode_List1
    while currentNode != None:

        hashTable[currentNode.value] = True
        currentNode = currentNode.nextnode


    currentNode = startNode_List2



    
    while currentNode != None:

        if  currentNode.value not in  hashTable:
            hashTable[currentNode.value] = True

        currentNode = currentNode.nextnode


    print("Union : {}".format(hashTable))


def getIntersection(startNode_List1,startNode_List2):
    hashTable = {}
    currentNode = startNode_List1
    while currentNode != None:
        hashTable[currentNode.value] = 0
        currentNode = currentNode.nextnode

    currentNode = startNode_List2

    while currentNode != None:

        if currentNode.value  in hashTable:
            hashTable[currentNode.value] = 1


        currentNode = currentNode.nextnode
    print("Intersection")
    for key in hashTable:
        if hashTable[key] == 1:
           print(key)


"""
List1: 10->15->4->20
   lsit2:  8->4->2->10
"""

a1 = SinglyListNode(10)
a2 = SinglyListNode(15)
a3 = SinglyListNode(4)
a4 = SinglyListNode(20)

a1.nextnode = a2
a2.nextnode = a3
a3.nextnode = a4


b1 = SinglyListNode(8)
b2 = SinglyListNode(4)
b3 = SinglyListNode(2)
b4 = SinglyListNode(10)

b1.nextnode = b2
b2.nextnode = b3
b3.nextnode = b4




getUnion(a1,b1)
getIntersection(a1,b1)



