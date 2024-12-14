class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        # print('push', data)
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return
        node = self.top
        self.top = node.next
        # print('pop', node.data, node.next)

    def result(self):
        cnt = 0
        node = self.top
        while node:
            # print(node.data)
            cnt += node.data
            node = node.next
        # print(node)
        return cnt

stack = Stack()
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.push(num)
print(stack.result())