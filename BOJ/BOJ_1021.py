# Baekjoon Online Judge - 1021번. 회전하는 큐

from collections import deque

N, M = map(int, input().split())
index_list = list(map(int, input().split()))
result = 0
q = deque([i for i in range(1, N + 1)])

for idx in index_list:
    if idx == q[0]:
        q.popleft()
    else:
        now = q.index(idx)
        # 현재의 큐에서 찾으려는 인덱스의 위치가 절반보다 작거나 같은경우 왼쪽으로 이동
        if now <= len(q) // 2:
            while q[0] != idx:
                q.rotate(-1)
                result += 1
        # 반대인 경우에는 오른쪽으로 이동
        else:
            while q[0] != idx:
                q.rotate(1)
                result += 1
        q.popleft() # 찾았으니 빼준다(맨 앞)
print(result)
