# Baekjoon Online Judge - 1719번. 택배
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                # start행부터 시작이 아닐까 오해할 수 있다.
                # 그러나, 현재 노드에서 최단 경로인 노드가 이전 노드를 나타내므로 result[i[0]][start] = now로 해야한다.
                # result[start][i[0]]으로 할 시, 예를 들어 1행 6열의 결과가 아닌 6행 1열의 결과가 저장이된다.
                result[i[0]][start] = now


INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = [['-'] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # 무방향 그래프
    graph[a].append((b, c))
    graph[b].append((a, c))

# 모든 노드의 시작으로부터 다른 모든 노드들의 최단경로를 구해야함
for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    for j in range(n + 1):
        if distance[j] == INF:
            distance[j] = '-'


for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(result[i][j], end=' ')
    print()
