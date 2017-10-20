
from Trees.BinaryNode import BinaryNode


def inOrder(root):

    if root != None:

        inOrder(root.leftChild)
        print(root.key)
        inOrder(root.rightChild)


def postOrder(root):

    if root != None:

        inOrder(root.leftChild)
        inOrder(root.rightChild)
        print(root.key)


def preOrder(root):

    if root != None:

        print(root.key)
        inOrder(root.leftChild)
        inOrder(root.rightChild)


rootNode = BinaryNode(4)
rootNode.leftChild = BinaryNode(2)
rootNode.leftChild.leftChild = BinaryNode(1)
rootNode.leftChild.rightChild = BinaryNode(3)

rootNode.rightChild = BinaryNode(7)
rootNode.rightChild.leftChild = BinaryNode(6)
rootNode.rightChild.rightChild = BinaryNode(8)


print("In Order...")
inOrder(rootNode)


print("\n preOrder...")
preOrder(rootNode)


print("\n postOrder...")
postOrder(rootNode)