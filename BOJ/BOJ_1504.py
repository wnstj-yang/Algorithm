# Baekjoon Online Judge - 1504번. 특정한 최단 경로
import heapq


def dijkstra(n):
    h = []
    dist = [INF] * (N + 1)
    dist[n] = 0
    heapq.heappush(h, (0, n))
    while h:
        # 현재 노드까지의 거리 node_dist, 현재 노드
        node_dist, node = heapq.heappop(h)
        # 현재노드까지의 거리가 최소 보다 크다면 끝
        if dist[node] < node_dist:
            continue

        for v, w in graph[node]:
            cost = node_dist + w
            # 현재까지의 거리가 저장된 최소 거리보다 작다면
            if cost < dist[v]:
                # 갱신해준다
                dist[v] = cost
                heapq.heappush(h, (cost, v))
    return dist


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = 10**9

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
start_1 = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

# 1 -> v1 -> v2 -> N
result1 = start_1[v1] + start_v1[v2] + start_v2[N]
# 1 -> v2 -> v1 -> N
result2 = start_1[v2] + start_v2[v1] + start_v1[N]

ans = min(result1, result2)
# ans != INF가 안되는 이유 => 그러한 경로가 없을 때
# INF이여야 -1을 출력하니까 적은걸로 표현해야한다
if ans < INF:
    print(ans)
else:
    print(-1)
