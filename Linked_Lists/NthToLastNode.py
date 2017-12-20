
from Linked_Lists.SinglyLinkedList import SinglyListNode

def nth_to_last_node(n, head):


    left_pointer = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in range(n - 1):

        # Check for edge case of not having enough nodes!
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer = right_pointer.nextnode

    # Move the block down the linked list
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    # Now return left pointer, its at the nth to last element!
    return left_pointer.value



a = SinglyListNode(1)
b = SinglyListNode(2)
c = SinglyListNode(3)
d = SinglyListNode(4)
e = SinglyListNode(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

print(nth_to_last_node(2,a))

