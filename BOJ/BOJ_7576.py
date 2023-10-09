# Baekjoon Online Judge - 7576번. 토마토

from collections import deque


def bfs():
    q = deque()
    for x, y in starts:
        q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == -1:
                continue

            if visited[nx][ny] == 0 and board[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                board[nx][ny] = 1


M, N = map(int, input().split())
# 좌우상하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
days = 0
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
starts = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            starts.append((i, j))
bfs()
for i in range(N):
    if 0 in board[i]:
        days = -1
        break
    days = max(days, max(visited[i]))
print(days)
