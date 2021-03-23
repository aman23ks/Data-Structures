class Stack(object):
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if self.item == []:
            return None
        else:
            return self.item.pop()

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []


def reverse(string):
    stack = Stack()
    tempStr = ""
    for i in range(len(string)):
        stack.push(string[i])

    while not stack.isEmpty():
        temp = stack.pop()
        tempStr = tempStr + temp

    return tempStr


print(reverse("aman"))
