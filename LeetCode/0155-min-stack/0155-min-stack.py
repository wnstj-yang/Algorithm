class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = [] # 최소값들을 계속 넣으며 변수명 그대로 최소값들의 스택이다.

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()