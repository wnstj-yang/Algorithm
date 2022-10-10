# Baekjoon Online Judge - 17143번. 낚시왕


def move_sharks():
    temp_board = [[[0, 0, 0] for _ in range(C)] for _ in range(R)] # 상어 보드 움직임에 따른 보드 초기화
    for i in range(R):
        for j in range(C):
            # 상어가 존재한다면
            if board[i][j] != [0, 0, 0]:
                speed, direction, size = board[i][j]
                x, y = i, j
                # 속력만큼 움직임 진행
                while speed:
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    # 격자 밖으로 나가게 된다면 방향만 바꿔준다
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        direction = change_direction(direction)
                        continue
                    x, y = nx, ny
                    speed -= 1
                # 새로운 보드에서 상어가 존재한다면
                if temp_board[x][y] != [0, 0, 0]:
                    # 사이즈가 큰 걸로 바꿔준다
                    if temp_board[x][y][2] < size:
                        temp_board[x][y] = [board[i][j][0], direction, size]
                # 존재하지 않을 경우에는 상어 넣어준다
                else:
                    temp_board[x][y] = [board[i][j][0], direction, size]

    return temp_board


# 각 방향 전환을 반대로 진행해준다. (상하우좌순서로 1 ~ 4)
def change_direction(num):
    if num == 1:
        return 2
    elif num == 2:
        return 1
    elif num == 3:
        return 4
    else:
        return 3


# 낚시꾼이 열마다 움직이면서 해당 열에서 가까운 상어를 잡고 0으로 초기화
def get_shark(idx):
    for i in range(R):
        if board[i][idx] != [0, 0, 0]:
            cnt = board[i][idx][2] # 크기
            board[i][idx] = [0, 0, 0]
            return cnt
    return 0


R, C, M = map(int, input().split())
board = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]
# 상하우좌
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
result = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = [s, d, z] # 속력, 방향, 크기

for j in range(C):
    result += get_shark(j)
    board = move_sharks()

print(result)

