class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.current = self.head

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def move(self, step, state):
        for _ in range(step):
            if state == 'U':
                self.current = self.current.prev
            else:
                self.current = self.current.next
        return self.current

    def update(self, data):
        node = self.head
        while node.data != data:
            node = node.next
        self.current = node


    def delete(self, data):
        # 1. 맨 앞을 삭제
        # 2. 맨 뒤를 삭제
        # 3. 이외의 경우 삭제
        if self.current == self.tail:
            self.current.prev.next = self.current.next
            self.current.prev = self.current.prev.prev
            self.current = self.current.prev
            self.tail = self.current
            return self.current
            # current 초기화

        elif self.current == self.head:
            self.current.next.prev = self.head.prev
            self.current = self.current.next
            self.head = self.current
            return self.current

            # current 초기화해주기
        else:
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.next
            return self.current


    def insert(self, info):
        self.desc()
        print(info.prev.data)
        print(self.tail.data)
        if info.prev is None:
            info.next.prev = info
            self.head = info
        elif info.next is None: # tail일 때
            info.prev.next = info
            # info.prev
            self.tail = info
        else:
            info.prev.next = info
            info.next.prev = info


    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next



def solution(n, k, cmd):
    answer = ''
    chart = DoubleLinkedList(0)
    stack = [] # 삭제된 최신의 것을 저장한다
    for i in range(1, n):
        chart.add(i)

    current = chart.current
    while current.data != k:
        current = current.next
    chart.update(k)
    # print(cmd)
    for info in cmd:
        print(info, current.data)
        if info[0] == 'C':
            stack.append(current)
            current = chart.delete(current)

        elif info[0] == 'Z':
            node = stack.pop()
            chart.insert(node)
        else:
            state, step = info.split()
            current = chart.move(int(step), state)

        # chart.desc()
        print('stack', stack)
        print('---------------------')
        # current = chart.current
    chart.desc()
    return answer

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
