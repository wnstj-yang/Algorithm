# Baekjoon Online Judge - 3190번. 뱀

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def move():
    x, y = 0, 0
    idx = 0 # 회전해야하는 정보의 위치 인덱스
    direction = 1 # 방향
    time = 1 # 시간
    snake = [(0, 0)] # 뱀의 길이에 대한 좌표 저장
    board[x][y] = 2
    while True:
        # 다음 좌표
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 범위를 벗어나거나 자신의 몸에 박았을 때 끝
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            return time
        # 사과가 아닌 경우 꼬리부분을 지워야함
        if board[nx][ny] == 0:
            i, j = snake.pop(0)
            board[i][j] = 0
        # 머리부분 이동된 것을 표시
        board[nx][ny] = 2
        snake.append((nx, ny))
        # 방향 바꾸어야할 시간이 됐을 때 바꿔준다
        if idx < len(rotate_info):
            if time == rotate_info[idx][0]:
                # 오른쪽 90도인 경우
                if rotate_info[idx][1] == 'D':
                    direction = (direction + 1) % 4
                else:
                    # 왼쪽 90도인 경우
                    direction = (direction - 1) % 4
                idx += 1
        time += 1
        x, y = nx, ny


N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())

rotate_info = []

for _ in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y] = 1

L = int(input())
for _ in range(L):
    x, y = map(str, input().split())
    x = int(x)
    rotate_info.append((x, y))

print(move())
