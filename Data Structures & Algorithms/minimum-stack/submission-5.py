class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        self.values = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.values[val] = self.values.get(val, 0) + 1
        if self.min_val == None or val < self.min_val:
            self.min_val = val

    def pop(self) -> None:
        val = self.stack.pop()
        self.values[val] -= 1
        if self.values[val] == 0:
            del self.values[val]
            # update min value
            self.min_val = min(self.values, default=None)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
