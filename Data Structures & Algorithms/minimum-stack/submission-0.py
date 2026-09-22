class MinStack:

    def __init__(self):
        self.stack = []
        minElement = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        minElement = float('inf')
        for i in self.stack:
            minElement = min(minElement, i)
        return minElement
