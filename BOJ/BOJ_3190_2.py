# Baekjoon Online Judge - 3190번. 뱀


def move_snake():
    snake = [(0, 0)]
    time = 1
    direction = 1
    x, y = 0, 0
    idx = 0
    board[x][y] = 2
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 뱀이 범위를 벗어나거나 자기 몸에 부딪히면 끝
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            return time

        # 사과아닐 때 몸 길이 줄임
        if board[nx][ny] == 0:
            a, b = snake.pop(0)
            board[a][b] = 0
        # 사과 존재하거나 비어있으면 머리가 증가되어 길이 증가
        board[nx][ny] = 2
        snake.append((nx, ny))
        # idx라는 변수를 활용해서 회전 해야되는 시간 체크
        if idx < len(rotate_info):
            if rotate_info[idx][0] == time:
                # 오른쪽이면 + 1 해서 방향을 나머지연산으로 상우하좌 형식으로 진행
                if rotate_info[idx][1] == 'D':
                    direction = (direction + 1) % 4
                # 왼쪽이면 - 1
                else:
                    direction = (direction - 1) % 4
                idx += 1
        # 시간 증가 및 좌표 옮기기
        time += 1
        x, y = nx, ny


# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1
L = int(input())
rotate_info = []
for _ in range(L):
    n, d = map(str, input().split())
    rotate_info.append((int(n), d))
result = move_snake()
print(result)
