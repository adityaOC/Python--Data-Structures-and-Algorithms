from Trees.BinaryNode import BinaryNode
from Stacks_and_Queue.Stacks.MyStack import MyStack


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


def preOrderIterative(root):

    if root == None:
        return

    stack1 = MyStack()
    stack1.push(root)
    while not stack1.isEmpty():

        node = stack1.pop()
        print(node.key)



        if node.rightChild != None:
            stack1.push(node.rightChild)
        if node.leftChild != None:
            stack1.push(node.leftChild)


def postOrderIterative(root):

    if root == None:
        return

    stack1 = MyStack()
    stack2 = MyStack()

    stack1.push(root)


    while not stack1.isEmpty():

        node = stack1.pop()

        if node.leftChild != None:
            stack1.push(node.leftChild)
        if node.rightChild != None:
            stack1.push(node.rightChild)

        stack2.push(node)

    while not stack2.isEmpty():
        node = stack2.pop()
        print(node.key)







a = BinaryNode(10)
a.leftChild = BinaryNode(5)
a.rightChild = BinaryNode(15)

a.leftChild.leftChild = BinaryNode(2)
a.leftChild.rightChild = BinaryNode(7)
a.rightChild.leftChild = BinaryNode(12)
a.rightChild.rightChild = BinaryNode(17)


#inOrder_Traversal(a)
#preOrder_Treversal(a)
#postOrder_Traversal(a)

#print("_____________________________")
#preOrderIterative(a)
#postOrderIterative(a)





