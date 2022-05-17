# Baekjoon Online Judge - 17396번. 백도어

import heapq, sys
input = sys.stdin.readline


def dijkstra():
    q = []
    distance = [INF] * N
    distance[0] = 0
    heapq.heappush(q, (0, 0))
    while q:
        d, now = heapq.heappop(q)
        if d > distance[now]:
            continue

        for node, time in graph[now]:
            cost = time + d
            # 시야를 밝혀주지 않는 곳으로 판단
            if cost < distance[node] and state[node] == 0:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    return distance


N, M = map(int, input().split())
state = list(map(int, input().split()))
state[-1] = 0 # 도착점은 시야를 밝히지만 무조건 도착해야하므로 시야를 밝히지 않는 것으로 정함
graph = [[] for _ in range(N)]
INF = int(1e11) # 최대 값이 300억이므로 최대 값을 1000억으로 설정
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

dist = dijkstra()
if dist[-1] == INF:
    print(-1)
else:
    print(dist[-1])
