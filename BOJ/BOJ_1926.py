# Baekjoon Online Judge - 1926번. 그림


from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    area_cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                area_cnt += 1
    return area_cnt


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_area = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j]:
            area = bfs(i, j)
            max_area = max(area, max_area)
            cnt += 1
print(cnt)
print(max_area)

