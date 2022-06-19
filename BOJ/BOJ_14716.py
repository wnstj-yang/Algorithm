# Baekjoon Online Judge - 14716번. 현수막

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

M, N = map(int, input().split())
graph = []
visited = [[False] * N for _ in range(M)]
result = 0
for _ in range(M):
    graph.append(list(map(int, input().split())))


for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            result += 1
            visited[i][j] = True
            q = []
            q.append((i, j))
            while q:
                x, y = q.pop(0)
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N:
                        continue
                    if not visited[nx][ny] and graph[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
print(result)
