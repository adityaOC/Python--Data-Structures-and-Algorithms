"""
This code reverses the linked list


"""

from Linked_Lists.SinglyLinkedList import SinglyListNode

def reverseList(SinglyListNode):

   currentNode = SinglyListNode
   prevNode = None
   nextNode = None

   while currentNode:

       # Make sure to copy the current nodes next node to a variable next_node
       # Before overwriting as the previous node for reversal
       nextNode = currentNode.nextnode

       # Reverse the pointer ot the next_node
       currentNode.nextnode = prevNode

       # Go one forward in the list
       prevNode = currentNode
       currentNode = nextNode


   return prevNode


# Create a list of 4 nodes
a = SinglyListNode(1)
b = SinglyListNode(2)
c = SinglyListNode(3)
d = SinglyListNode(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d




print(a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)



print("call reverse")

reverseList(a)

print (d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)

