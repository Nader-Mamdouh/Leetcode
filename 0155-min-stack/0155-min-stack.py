class MinStack:

    def __init__(self):
        self.stack = []
        self.mnstack =[]        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mnstack or val<=self.mnstack[-1]:
            self.mnstack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.mnstack and popped == self.mnstack[-1]:
            self.mnstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mnstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()