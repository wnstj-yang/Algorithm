# Baekjoon Online Judge - 11403번. 경로 찾기


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 거쳐가면서 갈 수 있는 노드가 늘어나면서 스스로에게도 갈 수 있음
for k in range(N): # 거쳐가는 노드
    for i in range(N):
        for j in range(N):
            # 현재 그래프상태에서 거쳐가서 방문할 수 있으면 가능하다고 표시 (0, 0)
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1
for i in graph:
    print(*i)
