class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head == None:
            return "Empty"
        else:
            values = ""
            current_node = self.head
            while current_node != None:
                values += str(current_node.data)
                values += " "
                current_node = current_node.next
        return values

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            current_node = self.head
            for i in range(self.length-2):
                current_node = current_node.next
            self.prev = current_node

    def insert(self, index, data):
        if index >= self.length:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        elif index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head
            current_node2 = self.head
            for i in range(index-1):
                current_node = current_node.next
            for i in range(index+1):
                current_node2 = current_node2.next
            new_node.next = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            current_node2.prev = new_node
            self.length += 1

    def remove(self, index):
        if index == 0:
            current_node = self.head
            current_node = current_node.next
            self.head = current_node
        else:
            current_node = self.head
            current_node2 = self.head
            for i in range(index-1):
                current_node = current_node.next
            for i in range(index+1):
                current_node2 = current_node2.next
            current_node.next = current_node2
            current_node2.prev = current_node
            self.length -= 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1


myDoublyLinkedList = DoublyLinkedList()
myDoublyLinkedList.append(3)
myDoublyLinkedList.append(5)
myDoublyLinkedList.append(8)
myDoublyLinkedList.prepend(2)
myDoublyLinkedList.insert(29, 9)
myDoublyLinkedList.insert(3, 7)
myDoublyLinkedList.insert(0, 6)
myDoublyLinkedList.remove(0)
myDoublyLinkedList.remove(0)
print(myDoublyLinkedList)
