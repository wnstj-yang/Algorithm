# Baekjoon Online Judge - 1303번. 전쟁 - 전투

from collections import deque

N, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
war = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
result = {'W': 0, 'B': 0}
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            q = deque()
            q.append((i, j))
            cnt = 1
            color = war[i][j]
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N:
                        continue
                    if not visited[nx][ny] and war[nx][ny] == color:
                        cnt += 1
                        visited[nx][ny] = True
                        q.append((nx, ny))
            result[color] += (cnt * cnt)
print(*result.values())
