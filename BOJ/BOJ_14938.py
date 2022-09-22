# Baekjoon Online Judge - 14938번. 서강그라운드


import heapq


def dijkstra(start):
    q = []
    INF = 987654321
    distance = [INF] * (N + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        for n, w in graph[now]:
            cost = dist + w
            if cost < distance[n]:
                heapq.heappush(q, (cost, n))
                distance[n] = cost

    return distance


N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
ans = 0
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

for i in range(1, N + 1):
    result = dijkstra(i)
    temp = 0
    for j in range(1, N + 1):
        if result[j] <= M:
            temp += items[j]
    ans = max(ans, temp)
print(ans)
