class MinStack:

    def __init__(self):
        self.current_min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # update the current min number
        if not self.current_min:
            self.current_min.append(val)
        else:
            new_num = min(val, self.current_min[-1])
            # we will add to the stack anyways if the val is bigger than the 
            # current minimum. This means that for this particular value
            # when we are capturing the state at which the stack currently is
            # so when we pop(), its ok to remove from the min stack
            # so if the val = 5 and current min is -1
            # its still [-1, -1] vs [0, 5], which is ok
            self.current_min.append(new_num)

    def pop(self) -> None:
        self.stack.pop()
        # update the current_min
        self.current_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
