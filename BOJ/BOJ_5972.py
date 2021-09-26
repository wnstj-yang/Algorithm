# Baekjoon Online Judge - 5972번. 택배 배송

# 다익스트라 우선순위 큐 이용(heapq) => 노드가 많기 때문
import heapq


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        print(q)
        # current_dist => cur_dist 현재 거리 값 , n은 현재 노드
        cur_dist, n = heapq.heappop(q)
        # 현재 노드까지의 거리가 저장된 거리보다 크다면 최소가 이미 아님
        if dist[n] < cur_dist:
            continue

        for i, w in graph[n]:
            # 연결된 노드까지의 가중치 게산
            if dist[i] > cur_dist + w:
                dist[i] = cur_dist + w
                heapq.heappush(q, (dist[i], i))


# 출발은 1, 도착지는 N
INF = 10 ** 9
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)
for _ in range(M):
    A_i, B_i, C_i = map(int, input().split())
    graph[A_i].append((B_i, C_i))
    graph[B_i].append((A_i, C_i))

dijkstra(1)
print(dist[N])
