from collections import deque


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 1:
                visited[nx][ny] += 1
            elif visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
time = 0
# 화면의 가장자리가 양 끝의 1개가 아니라 전체가 이어지는 부분이다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    result = 0
    for b in board:
        result += sum(b)

    if result == 0:
        print(time)
        break
    visited = [[0] * M for _ in range(N)]
    bfs()
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2 and board[i][j] == 1:
                board[i][j] = 0
    time += 1
