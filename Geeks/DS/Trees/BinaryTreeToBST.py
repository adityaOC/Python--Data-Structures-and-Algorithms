

class Node:

    def __init__(self,key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


def convert(rootNode):

    arr = arrayFromTree(rootNode)
    arr.sort()
    replaceSortedKeys(arr,rootNode)
    return rootNode


def replaceSortedKeys(arr,rootNode):

    if rootNode == None:
        return
    replaceSortedKeys(arr,rootNode.leftChild)
    rootNode.key = arr[0]
    arr.pop(0)
    replaceSortedKeys(arr,rootNode.rightChild)



def arrayFromTree(rootNode):

    arr = []
    arrayFromTreeHelper(rootNode,arr)
    return arr

def arrayFromTreeHelper(rootNode,arr):

    if rootNode == None:
        return

    arrayFromTreeHelper(rootNode.leftChild,arr)
    #print(rootNode.key)
    arr.append(rootNode.key)
    arrayFromTreeHelper(rootNode.rightChild,arr)


a = Node(10)
a.leftChild = Node(2)
a.rightChild = Node(7)
a.leftChild.leftChild = Node(8)
a.leftChild.rightChild = Node(4)

newBST = convert(a)
print("watch new tree in debugger ")
