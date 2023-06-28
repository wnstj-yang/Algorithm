# 최단거리 - 262p. 전보

import heapq


def dijkstra(start):
    distance[start] = 0 # 시작 노드는 거리가 0부터 시작
    q = [] # 우선순위 큐에 넣는 q
    heapq.heappush(q, (0, start)) # 앞에는 거리 비용, 노드 순으로 넣는다
    while q:
        dist, now = heapq.heappop(q)
        # 움직이면서 현재노드까지의 거리 비용과 최소값이 저장된 곳과 비교하여
        # 최소값의 테이블 보다 크면 이미 최소값으로 갈 수 없기 떄문에 넘어간다
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 노드와 가는데 드는 비용
        for node, cost in graph[now]:
            # 다음 노드까지의 최소 비용이 현재 새로 계산된 것보다 크면 갱신
            if dist + cost < distance[node]:
                distance[node] = dist + cost
                heapq.heappush(q, (dist + cost, node))


N, M, C = map(int, input().split())
INF = int(1e9)
graph = [[] * (N + 1) for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra(C)

cnt = 0
max_dist = 0 # 최대 거리를 한 이유는 최대한 많이 퍼져나가는 상황이므로
# 하나 갔다가 다시 돌아와서 가는 개념이 아니라 가장 멀리 퍼져나간 노드를 파악하는 것임
for d in distance[1:]:
    if d != INF:
        cnt += 1
        max_dist = max(max_dist, d)
print(cnt - 1, max_dist) # -1을 하는 이유는 출발 노드 C를 제외한 것이다.

