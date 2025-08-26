class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1],val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
    
lst=[2, 3, 4, 5, 6, 8, 10, 21, 24, 26]

TestStack=MinStack()

for i in lst:
    TestStack.push(i)
    
print(TestStack.minStack)
print(TestStack.stack)