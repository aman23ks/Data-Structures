# O(1) time and space complexity
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:

        if self.stack == []:
            self.stack.append(val)
            self.min = val
        elif val > self.min:
            self.stack.append(val)
        else:
            self.stack.append(2*val - self.min)
            self.min = val

    def pop(self) -> None:
        res = self.stack.pop()

        if res > self.min:
            pass
        else:
            self.min = 2*self.min - res
        return res

    def top(self) -> int:
        if not self.stack:
            return
        top = self.stack[-1]
        # ASK SOMEONE
        return min(max(-2147483648, top), 2147483647) if top >= self.min else self.min

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
