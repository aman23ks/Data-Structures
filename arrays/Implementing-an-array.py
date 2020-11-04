# Although arrays are predefined in python in the form of lists. we can implement our own arrays.
# Here we will implement our own arrays with some common methods such as access, push, pop, insert, delete.

class MyArray():
    def __init__(self):
        self.length = 0  # We initalize the array length to be zero
        # We initialize the data of array using an empty dictionary. The keys will corresspond to the index and the value to the data.
        self.data = {}

        # The attributes of the array class are stored in the dictionary by default .
        # when the __dict__ method is called on an instance of a class it returns the attributes of the class along with their attributes in dictionary format.
        # Now when the instance of the class is printed, it returns the class object with its location in memory.
        # But we know when we print an array we get the elements of the array as output
        # When we print the instance of the class, the built in __str__ method is called. So we can modify the __str__ method inside the class.
        # To suit our needs
    def __str__(self):
        # This will print the attributes of the array class(length and data) in string format when print(array_instance) is exectued.
        return str(self.__dict__)

    def get(self, index):
        # This element takes the index of the element as a parameter and returns it O(1) time.
        return self.data[index]

    def push(self, item):
        self.length += 1
        # Adds the item provided to the end of the array - time complexity O(1).
        self.data[self.length-1] = item

    def pop(self):
        last_item = self.data[self.length-1]  # Collects the last element
        del self.data[self.length-1]  # deletes the last element from the array
        self.length -= 1  # decrements the length of the array
        return last_item  # returns the popped item

    def insert(self, index, item):
        self.length += 1
        for i in range(self.length-1, index, -1):
            # Shifts every element from the index one place towards the right . Thus making space at the specified index.
            self.data[i] = self.data[i-1]
        # Adds the element at the given index O(n) Operation.
        self.data[index] = item

    def delete(self, index):
        for i in range(index, self.length-1):
            # Shifts elements from the given index to the end by one place towards left
            self.data[i] = self.data[i+1]
        # The last element which remains two times in the array is deleted
        del self.data[self.length-1]
        self.length -= 1  # The lenght is decremented by 1. O(n) operation


arr = MyArray()
arr.push(6)
#{'length': 1, 'data': {0: 6}}

arr.push(2)
#{'length': 2, 'data': {0: 6, 1: 2}}

arr.push(9)
#{'length': 3, 'data': {0: 6, 1: 2, 2: 9}}

arr.pop()
#{'length': 2, 'data': {0: 6, 1: 2}}

arr.push(45)
arr.push(12)
arr.push(67)
#{'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 12, 4: 67}}

arr.insert(3, 10)
#{'length': 6, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 12, 5: 67}}

arr.delete(4)
#{'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 67}}

print(arr.get(1))
# 2

print(arr)
# The outputs given after each function call are the outputs obtained by calling print(arr) and not by the function calls themselves
