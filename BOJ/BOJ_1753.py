# Baekjoon Online Judge - 1753번. 최단 경로
# 다익스트라 기본 틀로는 노드 갯수가 많기 때문에 시간 초과가 나온다
# 우선순위 큐를 이용해야함

import heapq


def dijkstra(s):
    h = []
    dist[s] = 0
    heapq.heappush(h, (0, s))
    while h:
        # node_list : 현재 노드까지의 거리 / node : 현재 노드
        node_dist, node = heapq.heappop(h)
        # 현재 노드가 이미 처리가 되었을 때, 최소값이 만들어 지지 안는 경우
        # 방문 체크 겸 부분
        if dist[node] < node_dist:
            continue

        # 다음 노드와 가중치
        for v, w in graph[node]:
            cost = node_dist + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(h, (cost, v))


V, E = map(int, input().split())
K = int(input())
# 무한 값
INF = 10**9
graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    # 방향 그래프
    graph[u].append((v, w))

dijkstra(K)
for val in dist[1:]:
    if val == INF:
        print('INF')
    else:
        print(val)
