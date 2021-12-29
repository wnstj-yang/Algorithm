# Baekjoon Online Judge - 1956번. 운동
# pypy3에서만 통과

# 방향성 그래프
# 플로이드 와샬로 자기 자신 사이클 체크

V, E = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (V + 1) for _ in range(V + 1)]
result = INF # 최소인 것을 찾는다
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 와샬 알고리즘 실행 부분
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 계산
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            # a -> b로 가는 최단 거리 보다 a -> k -> b
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 생겨진 사이클에서 최소인 것을 구한다
for i in range(1, V + 1):
    if graph[i][i] < result:
        result = graph[i][i]
# 운동 경로를 찾지 못하면 -1 출력
if result == INF:
    print(-1)
else:
    print(result)

