# DFS/BFS - 유형별 문제. 특정 거리의 도시 찾기 339p
# https://www.acmicpc.net/problem/18352

import heapq
import sys

input = sys.stdin.readline


def dijkstra(s):
    q = []
    INF = 987654321
    distance = [INF] * (N + 1)
    distance[s] = 0
    heapq.heappush(q, (0, s))
    result = []
    while q:
        d, now = heapq.heappop(q)
        if d > distance[now]:
            continue

        for i in board[now]:
            # 현재 노드까지의 거리와 연결된 다음 노드까지의 거리 가중치
            cost = d + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    for i in range(len(distance)):
        if distance[i] == K:
            result.append(i)

    return result


N, M, K, X = map(int, input().split())
board = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    board[x].append((y, 1))

answer = dijkstra(X)
if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)
