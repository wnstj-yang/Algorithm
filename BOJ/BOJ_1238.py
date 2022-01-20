# Baekjoon Online Judge - 1238번. 파티

import heapq


def dijkstra(n):
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, n))
    distance[n] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재노드 까지의 거리가 최단 거리 테이블에 있는 현재노드보다 크다면 이미 방문처리됨으로 인식
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1] # 현재노드에 연결된 간선노드까지의 총 비용
            if cost < distance[i[0]]: # 구한 총 비용이 최단 거리 테이블보다 작을 경우 초기화
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


N, M, X = map(int, input().split())
graph = [[] * (M + 1) for _ in range(N + 1)]
answer = 0
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
INF = 1e9
# X에서 되돌아가는 모드까지의 최단 거리 테이블
dist_back = dijkstra(X)

for i in range(1, N + 1):
    if i == X:
        continue
    dist_go = dijkstra(i) # i번부터 출발한 모든 노드와의 최단거리 테이블
    time = dist_go[X] + dist_back[i] # i번 노드에서 X번, X번에서 i번 노드까지 걸리는 시간
    if time > answer:
        answer = time
print(answer)

