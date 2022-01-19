# Baekjoon Online Judge - 14284번. 간선 이어가기 2
#
import heapq


def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0
    while q:
        # dist는 now(현재)노드까지의 최소 거리
        dist, now = heapq.heappop(q)
        # 현재 노드까지의 거리가 최소거리로 저장된 것 보다 크다면
        # 방문할 필요 X, 이미 크기 때문에
        if dist > distance[now]:
            continue
        # 연결된 간선
        for i in graph[now]:
            # 비용
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m = map(int, input().split())

graph = [[] * (m + 1) for _ in range(n + 1)]
INF = 1e9
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int ,input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))
s, t = map(int, input().split())
dijkstra(s)
print(distance[t])
