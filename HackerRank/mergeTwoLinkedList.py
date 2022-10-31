class Node:
    def __init__(self,
                 data):
        self.value = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self,
                  value,
                  location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
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


def mergeTwoLists(list1,
                  list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.value < list2.value:
        temp = head = Node(list1.value)
        list1 = list1.next
    else:
        temp = head = Node(list2.value)
        list2 = list2.next

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            temp.next = Node(list1.value)
            list1 = list1.next
        else:
            temp.next = Node(list2.value)
            list2 = list2.next
        temp = temp.next

    while list1 is not None:
        temp.next = Node(list1.value)
        list1 = list1.next
        temp = temp.next
    while list2 is not None:
        temp.next = Node(list2.value)
        list2 = list2.next
        temp = temp.next
    return head


newList = linkedList()
newList.insertSLL(4, 0)
newList.insertSLL(2, 0)
newList.insertSLL(1, 0)
print([node.value for node in newList])
oldList = linkedList()
oldList.insertSLL(4, 0)
oldList.insertSLL(3, 0)
oldList.insertSLL(1, 0)
print([node.value for node in oldList])

node = mergeTwoLists(newList.head, oldList.head)

while node:
    print(node.value)
    node = node.next