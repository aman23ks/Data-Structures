# Implementation of a stack using linked list.

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        if self.length == 0:
            print("Empty")
        else:
            values = ""
            current_value = self.top
            while current_value != None:
                values += str(current_value.data)
                values += " "
                current_value = current_value.next
        return values

    def push(self, data):
        new_value = Node(data)
        if self.length == 0:
            self.top = new_value
            self.bottom = new_value
            self.length += 1
        else:
            self.bottom.next = new_value
            self.bottom = new_value
            self.length += 1

    def pop(self):
        current_value = self.top
        for i in range(self.length-2):
            current_value = current_value.next
        current_value.next = None
        self.length -= 1

    def peek(self):
        current_value = self.top
        while current_value.next:
            current_value = current_value.next
        return print(current_value.data)


myStack = Stack()
myStack.push(3)
myStack.push(5)
myStack.push(6)
myStack.push(1)
myStack.push(4)
myStack.push(2)
myStack.pop()

myStack.peek()
print(myStack)
