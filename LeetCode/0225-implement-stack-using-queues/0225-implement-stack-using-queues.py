class MyStack(object):

    def __init__(self):
        self.q = []
        

    def push(self, x):
        self.q.append(x)
        

    def pop(self):
        return self.q.pop()
        

    def top(self):
        if self.q:
            return self.q[-1]
        return 'null'
        

    def empty(self):
        if self.q:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# print(obj.q)
# obj.pop()
# print(obj.q)
# print(obj.top())
# print(obj.q)
# print(obj.empty())
# print(obj.q)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()