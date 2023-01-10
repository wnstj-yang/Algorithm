# Baekjoon Online Judge - 2161번. 카드1

from collections import deque

N = int(input())
q = deque(range(1, N + 1))
ans = []
while len(q) > 1:
    ans.append(q.popleft())
    q.append(q.popleft())
ans.append(q.pop())
print(*ans)
