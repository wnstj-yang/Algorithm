# Baekjoon Online Judge - 1916번. 최소비용 구하기

import heapq


def dijkstra(n):
    q = []
    heapq.heappush(q, (0, n))
    distance[n] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 거리가 크다면 체크하지 않음과 동시에 방문 표시를 한다.
        if distance[now] < dist:
            continue

        for info in graph[now]:
            # 현재까지 걸린 가중치와 현재노드와 연결된 다음 노드의 가중치 합
            cost = info[1] + dist
            # 위의 cost가 현재 거리 테이블에 있는 것보다 작으면 초기화
            if cost < distance[info[0]]:
                distance[info[0]] = cost
                heapq.heappush(q, (cost, info[0]))


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
INF = int(1e9)
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
s, e = map(int, input().split())
dijkstra(s)
print(distance[e])
