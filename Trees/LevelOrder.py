from Trees.BinaryNode import BinaryNode
from Stacks_and_Queue.Queues.MyQueue import MyQueue
import collections

root = BinaryNode(1)
root.leftChild = BinaryNode(2)
root.rightChild = BinaryNode(3)
root.leftChild.leftChild = BinaryNode(4)
root.leftChild.rightChild = BinaryNode(5)
root.rightChild.leftChild = BinaryNode(6)
root.rightChild.rightChild = BinaryNode(7)

root2 = BinaryNode(1)
root2.leftChild = BinaryNode(2)
root2.rightChild = BinaryNode(3)
root2.leftChild.leftChild = BinaryNode(4)
root2.leftChild.rightChild = BinaryNode(5)
root2.rightChild.leftChild = BinaryNode(6)
root2.rightChild.rightChild = BinaryNode(7)

#root2.leftChild.leftChild.leftChild = BinaryNode(9)
root2.leftChild.leftChild.rightChild = BinaryNode(10)

#root2.rightChild.rightChild.rightChild = BinaryNode(11)


def levelOrder(root):
    q = MyQueue()
    q.enqueue(root)
    q.enqueue(None)
    arr = [root.key]
    print(arr)
    arr = []


    while not q.isEmpty():

        top = q.dequeue()
        if top == None and q.size() >=1:
            """if top is None and after dequeue, queue size is 0 (q.size() >=1 is false) 
            
            then tree traversal is finished"""
            print("\n")

            print(arr)
            arr = []

            q.enqueue(top)

        elif top :

            if top.leftChild:
                q.enqueue(top.leftChild)
                arr.append(top.leftChild.key)
            if top.rightChild:
                q.enqueue(top.rightChild)
                arr.append(top.rightChild.key)

        #q.displayAllElements()





levelOrder(root2)

