class MaxHeap:
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
        if(self.hasParent(index) and self.parent(index) < self.storage[index]):
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
        while(self.hasParent(index) and self.parent(index) < self.storage[index]):
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
        largest = index
        if(self.hasLeftChild(index) and self.storage[largest] < self.leftChild(index)):
            largest = self.getLeftChildIndex(index)
        if(self.hasRightChild(index) and self.storage[largest] < self.rightChild(index)):
            largest = self.getRightChildIndex(index)
        if(largest != index):
            self.swap(index, largest)
            self.heapifyDownRecursive(largest)

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
            largerChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                largerChildIndex = self.getRightChildIndex(index)
            if(self.storage[index] < self.storage[largerChildIndex]):
                break
            else:
                self.swap(index, largerChildIndex)
            index = largerChildIndex

    # Removal from a min heap #

    def printHeap(self):
        return print(self.storage)


maxheap = MaxHeap(10)
maxheap.insertRecursive(20)
maxheap.insertRecursive(5)
maxheap.insertRecursive(12)
maxheap.insertRecursive(8)
maxheap.insertRecursive(9)
maxheap.insertRecursive(30)
# maxheap.insertRecursive(6)
# maxheap.insertRecursive(2)
# maxheap.insertRecursive(9)
# maxheap.insertRecursive(10)
maxheap.removeMinRecursive()
maxheap.removeMinRecursive()
# maxheap.removeMinRecursive()
# maxheap.removeMinRecursive()
maxheap.printHeap()
