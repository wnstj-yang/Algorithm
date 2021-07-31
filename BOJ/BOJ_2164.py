# Baekjoon Online Judge - 2164번. 카드2
# deque가 아닐 때는 시간초과
from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
