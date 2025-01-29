class MinStack:

    def __init__(self):
        self.q = []

    def push(self, val: int) -> None:
        curMin = self.getMin()
        if curMin is None or val < curMin:
            curMin = val
        self.q.append((val, curMin))

    def pop(self) -> None:
        if self.q:
            self.q.pop()

    def top(self) -> int:
        if not self.q:
            return None
        return self.q[-1][0]

    def getMin(self) -> int:
        if not self.q:
            return None
        return self.q[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()