# 구현 - 유형별 문제. 뱀 521p

from collections import deque


def move_snake():
    snake = deque()
    snake.append((0, 0))
    x, y = 0, 0 # 뱀 머리 위치
    board[x][y] = 2 # 뱀
    time = 1
    d = 0
    idx = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            return time
        if board[nx][ny] == 0:
            a, b = snake.popleft()
            board[a][b] = 0
        snake.append((nx, ny))
        board[nx][ny] = 2
        if idx < len(rotate_info):
            if time == rotate_info[idx][0]:
                if rotate_info[idx][1] == 'D':
                    d = (d + 1) % 4
                else:
                    d = (d - 1) % 4
                idx += 1
        time += 1
        x, y = nx, ny


# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1
rotate_info = []
L = int(input())
for _ in range(L):
    t, d = map(str, input().split())
    rotate_info.append((int(t), d))
print(move_snake())
