# 최단 경로 - 259p. 미래 도시

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
# 양방향이므로 각각 1로 초기화
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split()) # X를 거쳐 K로 가는 최단 거리(1번 노드부터 출발)
# O(N^3)의 시간복잡도를 가지는 플로이드 와샬 
# 1번 -> X -> K까지의 정해진 경로가 있기에 해당 부분만 살펴보는게 아닌가 싶었지만,
# 중간에 노드가 존재할 수도 있고 그에 따른 최단 경로도 필요하기 때문에 모두 돌아간다고 봐야한다
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][K] + graph[K][X] # 1 -> X -> K까지의 최단 경로

# 최단 경로를 구하지 못하면 -1로 출력
if result == INF:
    print(-1)
else:
    print(result)