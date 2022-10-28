class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # Creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created."

    # Insertion of a node in circular SLL
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted."

    # Traversal of a node in circular SLL
    def traversalCSLL(self):
        if self.head is None:
            print("The Circular Singly Linked List does not exist.")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break


circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(20, 0)
circularSLL.insertCSLL(200, 1)
circularSLL.insertCSLL(10, 1)
circularSLL.insertCSLL(50, 2)
print([node.value for node in circularSLL])
circularSLL.traversalCSLL()