from Stacks_and_Queue.Queues.MyQueue import MyQueue

from Linked_Lists.SinglyLinkedList import SinglyListNode
from Trees.BinaryNode import BinaryNode
from Trees.Traversal import inOrder_Traversal


def constructBST(listRoot):

    queue = MyQueue()
    treeRoot = BinaryNode(listRoot.value)

    originalTreeRoot = treeRoot

    isRoot = True
    while listRoot != None:


        listRoot = listRoot.nextnode
        if listRoot:
            treeRoot.leftChild = BinaryNode(listRoot.value)
            queue.enqueue(treeRoot.leftChild )
        else:
            break

        listRoot = listRoot.nextnode

        if listRoot:
            treeRoot.rightChild = BinaryNode(listRoot.value)
            queue.enqueue( treeRoot.rightChild)
        else:
            break
        treeRoot = queue.dequeue()

    return originalTreeRoot

la = SinglyListNode(10)
lb = SinglyListNode(12)
lc = SinglyListNode(15)
ld = SinglyListNode(25)
le = SinglyListNode(30)
lf = SinglyListNode(36)

la.nextnode = lb
lb.nextnode = lc
lc.nextnode = ld
ld.nextnode = le
le.nextnode = lf

root = constructBST(la)
inOrder_Traversal(root)


#--------------------------------------------------------


"""
# its linked list representation

# Linked List node
class ListNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Binary Tree Node structure
class BinaryTreeNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Class to convert the linked list to Binary Tree
class Conversion:
    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self, data=None):
        self.head = None
        self.root = None

    def push(self, new_data):

        # Creating a new linked list node and storing data
        new_node = ListNode(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Move the head to point to new node
        self.head = new_node

    def convertList2Binary(self):

        # Queue to store the parent nodes
        q = []

        # Base Case
        if self.head is None:
            self.root = None
            return

        # 1.) The first node is always the root node,
        # and add it to the queue
        self.root = BinaryTreeNode(self.head.data)
        q.append(self.root)

        # Advance the pointer to the next node
        self.head = self.head.next

        # Until th end of linked list is reached, do:
        while (self.head):

            # 2.a) Take the parent node from the q and
            # and remove it from q
            parent = q.pop(0)  # Front of queue

            # 2.c) Take next two nodes from the linked list.
            # We will add them as children of the current
            # parent node in step 2.b.
            # Push them into the queue so that they will be
            # parent to the future node
            leftChild = None
            rightChild = None

            leftChild = BinaryTreeNode(self.head.data)
            q.append(leftChild)
            self.head = self.head.next
            if (self.head):
                rightChild = BinaryTreeNode(self.head.data)
                q.append(rightChild)
                self.head = self.head.next

            # 2.b) Assign the left and right children of parent
            parent.left = leftChild
            parent.right = rightChild

    def inorderTraversal(self, root):
        if (root):
            self.inorderTraversal(root.left)
            print(root.data)
            self.inorderTraversal(root.right)


# Driver Program to test above function

# Object of conversion class
conv = Conversion()
conv.push(36)
conv.push(30)
conv.push(25)
conv.push(15)
conv.push(12)
conv.push(10)

conv.convertList2Binary()

print("Inorder Traversal of the contructed Binary Tree is:{}".format(conv.inorderTraversal(conv.root)))

"""