class MinHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    # Helper Methods:

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def getParentIndex(self, index):
        return (index - 1) // 2

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    # Helper Methods #

    # Insertion into a min heap

    def insertRecursive(self, data):
        if(self.isFull()):
            return "Heap is Full"
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUpRecursive(self.size - 1)

    def heapifyUpRecursive(self, index):
        if(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(index, self.getParentIndex(index))
            self.heapifyUpRecursive(self.getParentIndex(index))

    def insertIterative(self, data):
        if(self.isFull()):
            return "Heap is Full"
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUpIterative()

    def heapifyUpIterative(self):
        index = self.size - 1
        while(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    # Insertion into a min heap #

    # Removal from a min heap

    def removeMinRecursive(self):
        if(self.size == 0):
            return "Empty Heap"
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDownRecursive(0)
        return print(data)

    def heapifyDownRecursive(self, index):
        smallest = index
        if(self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index)):
            smallest = self.getLeftChildIndex(index)
        if(self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index)):
            smallest = self.getRightChildIndex(index)
        if(smallest != index):
            self.swap(index, smallest)
            self.heapifyDownRecursive(smallest)

    def removeMinIterative(self):
        if(self.size == 0):
            return "Empty Heap"
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDownIterative()
        return data

    def heapifyDownIterative(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            if(self.storage[index] < self.storage[smallerChildIndex]):
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

    # Removal from a min heap #

    def printHeap(self):
        return print(self.storage)


minheap = MinHeap(10)
minheap.insertRecursive(20)
minheap.insertRecursive(5)
minheap.insertRecursive(12)
minheap.insertRecursive(8)
minheap.insertRecursive(9)
minheap.insertRecursive(3)
minheap.insertRecursive(6)
minheap.insertRecursive(2)
minheap.insertRecursive(9)
minheap.insertRecursive(10)
minheap.removeMinRecursive()
minheap.removeMinRecursive()
minheap.removeMinRecursive()
minheap.removeMinRecursive()
minheap.printHeap()
