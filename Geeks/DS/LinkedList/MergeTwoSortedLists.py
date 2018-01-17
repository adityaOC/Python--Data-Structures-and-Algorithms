
class Node:

    def __init__(self,key):
        self.key = key
        self.nextNode = None



def mergeList(list1,list2):

    sortedList = None

    p = list1
    q = list2

    if p.key< q.key:

        sortedList = p
        p = p.nextNode
    else:
        sortedList = q
        q = q.nextNode

    returnSorted = sortedList

    while p and q:

        if p.key< q.key:
            sortedList.nextNode = p
            sortedList = sortedList.nextNode
            p = p.nextNode
        else:
            sortedList.nextNode = q
            sortedList = sortedList.nextNode
            q = q.nextNode


    while p :
        sortedList.nextNode = p
        sortedList = sortedList.nextNode
        p = p.nextNode

    while q:
        sortedList.nextNode = q
        sortedList = sortedList.nextNode
        q = q.nextNode

    return returnSorted


a1 = Node(10)
a2 = Node(12)
a3 = Node(30)
a4 = Node(40)
a5 = Node(50)
a6 = Node(60)

a1.nextNode = a2
a2.nextNode = a3
a3.nextNode = a4
a4.nextNode = a5
a5.nextNode = a6

b1 = Node(15)
b2 = Node(25)
b3 = Node(26)
b4 = Node(45)

b1.nextNode= b2
b2.nextNode = b3
b3.nextNode = b4



sortedList = mergeList(b1,a1)

while sortedList:
    print(sortedList.key)
    sortedList = sortedList.nextNode

