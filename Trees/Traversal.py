from Trees.BinaryNode import BinaryNode


def inOrder_Traversal(rootNode):

    #print(rootNode.leftChild.key)
    #return
    if rootNode:
        inOrder_Traversal(rootNode.leftChild)
        print(rootNode.key)
        inOrder_Traversal(rootNode.rightChild)
    else:
        return


def preOrder_Treversal(rootNode):

    if rootNode:

        print(rootNode.key)
        preOrder_Treversal(rootNode.leftChild)
        preOrder_Treversal(rootNode.rightChild)
    else:
        return

def postOrder_Traversal(rootNode):

    if rootNode:
        postOrder_Traversal(rootNode.leftChild)
        postOrder_Traversal(rootNode.rightChild)
        print(rootNode.key)
    else:
        return


a = BinaryNode(10)
a.leftChild = BinaryNode(5)
a.rightChild = BinaryNode(15)

a.leftChild.leftChild = BinaryNode(2)
a.leftChild.rightChild = BinaryNode(7)
a.rightChild.leftChild = BinaryNode(12)
a.rightChild.rightChild = BinaryNode(17)


#inOrder_Traversal(a)
#preOrder_Treversal(a)
postOrder_Traversal(a)





