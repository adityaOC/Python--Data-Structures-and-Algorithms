
"""
This code checks if there is cycle present in linked list

"""

from Linked_Lists.SinglyLinkedList import SinglyListNode

def checkCycle(SinglyListNode):


    slow = SinglyListNode
    fast = SinglyListNode

    while fast != None and fast.nextnode != None :

        slow = slow.nextnode
        fast = fast.nextnode.nextnode

        if slow == fast:
            return True

    return False






a = SinglyListNode(1)
b = SinglyListNode(2)
c = SinglyListNode(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!

print(checkCycle(a))

x = SinglyListNode(1)
y = SinglyListNode(2)
z = SinglyListNode(3)

x.nextnode = y
y.nextnode = z
print(checkCycle(x))