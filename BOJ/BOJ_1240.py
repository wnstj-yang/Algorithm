# Baekjoon Online Judge - 1240번. 노드사이의 거리

from collections import deque


def bfs(start, end):
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque()
    q.append((start, 0))
    while q:
        now, cost = q.popleft()
        if now == end:
            return cost
        for t, d in graph[now]:
            if not visited[t]:
                visited[t] = True
                q.append((t, cost + d))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))
