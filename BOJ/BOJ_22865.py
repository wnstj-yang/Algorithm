# Baekjoon Online Judge - 22865번. 가장 먼 곳
# pypy3로 통과
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF] * (N + 1) # 노드들의 최단경로를 저장할 리스트
    dist[start] = 0 # 출발점
    while q:
        # now노드까지의 d(최단거리)
        d, now = heapq.heappop(q)
        # visited표시 대신 현재 노드의 최단거리가 저장된 리스트의 값보다 크면
        if dist[now] < d:
            continue
        # 현재노드와 연결된 노드들
        for i in places[now]:
            cost = d + i[1] # 연결된 노드 까지의 비용(최단거리)
            if cost < dist[i[0]]: #
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # 최소값을 넣어준다
    for i in range(1, N + 1):
        if i not in friends:
            dist_result[i] = min(dist_result[i], dist[i])


N = int(input())
friends = list(set(map(int, input().split())))
M = int(input())
places = [[] for _ in range(N + 1)]
INF = int(1e9)
max_dist = 0
answer = 0
for _ in range(M):
    D, E, L = map(int, input().split())
    places[D].append((E, L))
    places[E].append((D, L))

dist_result = [INF] * (N + 1)
# 1~N+1까지의 노드부터 A, B, C를 구하기보다
# 무방향 그래프이므로 A, B, C로부터 각 노드들의 최소값을 구한다
for f in friends:
    dijkstra(f)

# 최소거리들 중 최대값을 구한다.
for i in range(1, N + 1):
    if dist_result[i] != INF:
        if max_dist < dist_result[i]:
            max_dist = dist_result[i]
            answer = i
print(answer)
