# Softeer - 장애물 인식 프로그램

from collections import deque


def search(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = num
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = num
                q.append((nx, ny))
                cnt += 1
    return cnt


N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
num = 1
blocks = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            blocks.append(search(i, j))
            num += 1
blocks.sort()
print(len(blocks))
for b in blocks:
    print(b)