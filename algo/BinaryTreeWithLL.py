import QueueLinkedList as queue


class TreeNode:
    def __init__(self,
                 data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# pre order binary tree traversal
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


newBT = TreeNode("Data Structure")
linear = TreeNode("Linear")
nonLinear = TreeNode("Non Linear")
array = TreeNode("Array")
linkedList = TreeNode("Linked List")
newBT.leftChild = linear
newBT.rightChild = nonLinear
linear.leftChild = array
linear.rightChild = linkedList


# print("#" * 5 + ' Pre Order Traversal ' + "#" * 5)
# preOrderTraversal(newBT)


# in order binary tree traversal
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# print("#" * 5 + ' In Order Traversal ' + "#" * 5)
# inOrderTraversal(newBT)


# post order binary tree traversal
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


# print("#" * 5 + ' Post Order Traversal ' + "#" * 5)
# postOrderTraversal(newBT)


# Level order binary tree traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


# print("#" * 5 + ' Level Order Traversal ' + "#" * 5)
# levelOrderTraversal(newBT)


# Search binary tree
def searchBT(rootNode,
             nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not Found"


# print(searchBT(newBT, "Array"))


# Insert node in Binary Tree
def insertNodeBT(rootNode,
                 newNode):
    if not rootNode:
        rootNode = newNode()
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)
        while not (customQ.isEmpty()):
            root = customQ.dequeue()
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"


newNode = TreeNode("New Algo")
insertNodeBT(newBT, newNode)


# levelOrderTraversal(newBT)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode


# print("#" * 5 + ' Deepest Node ' + "#" * 5)
# deepestNode = getDeepestNode(newBT)
# print(deepestNode.data)

def deleteDeepestNode(rootNode,
                      dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)


print("first one" + "#" * 5)
# levelOrderTraversal(newBT)
print(getDeepestNode(newBT).data)
deleteDeepestNode(newBT, getDeepestNode(newBT))
print("after deletion" + "#" * 5)
levelOrderTraversal(newBT)


def deleteNodeBT(rootNode,
                 node):
    if not rootNode:
        return "The BT does nto exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "This node has been successfully deleted"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"


def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"
