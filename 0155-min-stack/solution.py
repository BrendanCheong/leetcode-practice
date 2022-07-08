TOP = -1

class MinStack:

    def __init__(self):
        self.norm_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.norm_stack.append(val)
        if (not len(self.min_stack)):
            self.min_stack.append(val)
            return

        min_stack_top = self.min_stack[TOP]
        if (val <= min_stack_top):
            self.min_stack.append(val)

    def pop(self) -> None:
        if (self.min_stack[TOP] == self.norm_stack[TOP]):
            self.min_stack.pop()
        
        self.norm_stack.pop()

    def top(self) -> int:
        return self.norm_stack[TOP]
        
    def getMin(self) -> int:
        return self.min_stack[TOP]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
