class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini) == 0:
            self.mini.append(val)
        else:
            if self.mini[0] >= val:
                self.mini.insert(0,val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        poped = self.stack.pop()
        if poped == self.mini[0]:
            self.mini.pop(0)

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.mini) == 0:
            return None
        return self.mini[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()