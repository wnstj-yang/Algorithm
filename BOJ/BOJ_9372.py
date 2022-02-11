# Baekjoon Online Judge - 9372번. 상근이의 여행

from collections import deque


def bfs(s):
    global cnt
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        n = q.popleft()
        for i in flight_schedule[n]:
            if not visited[i]:
                cnt += 1
                q.append(i)
                visited[i] = True


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    flight_schedule = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())
        flight_schedule[a].append(b)
        flight_schedule[b].append(a)

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
    print(cnt)
