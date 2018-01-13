from Linked_Lists.SinglyLinkedList import LinkedList,SinglyListNode



def reverse(head):

    prevNode = None
    currentNode = head
    nextNode = head.nextnode

    while currentNode!=None:

        currentNode.nextnode = prevNode

        prevNode = currentNode
        currentNode = nextNode

        if nextNode == None:
            break
        nextNode = nextNode.nextnode

    return prevNode




a = SinglyListNode(10)
b = SinglyListNode(20)
c = SinglyListNode(30)
d = SinglyListNode(40)
e = SinglyListNode(50)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e



newHead = reverse(a)
print("\n\nRevered ")
node = newHead
while node!=None:

    print(node.value)
    node = node.nextnode



