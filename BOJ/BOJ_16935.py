# Baekjoon Online Judge - 16935번. 배열 돌리기 3

# 상하반전
def up_down(N, M):
    for j in range(M):
        for i in range(N // 2):
            arr[i][j], arr[-1-i][j] = arr[-1-i][j], arr[i][j]


# 좌우 반전
def left_right(N, M):
    for i in range(N):
        for j in range(M // 2):
            arr[i][j], arr[i][-1-j] = arr[i][-1-j], arr[i][j]


# 오른쪽으로 90도 회전
def right_degree_90(N, M):
    global arr
    temp = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            temp[j][N-1-i] = arr[i][j]
    arr = [item[:] for item in temp]


# 왼쪽으로 90도 회전
def left_degree_90(N, M):
    global arr
    temp = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            temp[M-1-j][i] = arr[i][j]
    arr = [item[:] for item in temp]


# 시계방향으로 4번 나누어진 것을 이동
def clockwise(N, M):
    global arr
    temp = [[0] * M for _ in range(N)]
    x = N // 2 # 3
    y = M // 2 # 4
    # 좌 -> 우
    for i in range(x):
        for j in range(y):
            temp[i][y+j] = arr[i][j]
    # 상 -> 하
    for i in range(x):
        for j in range(y, M):
            temp[x+i][j] = arr[i][j]
    # 우 -> 좌
    for i in range(x, N):
        for j in range(y, M):
            temp[i][j-y] = arr[i][j]
    # 하 -> 상
    for i in range(x, N):
        for j in range(y):
            temp[i-x][j] = arr[i][j]

    arr = [item[:] for item in temp]


# 반시계방향으로 4번 나누어진 것을 이동
def counterclockwise(N, M):
    global arr
    temp = [[0] * M for _ in range(N)]
    x = N // 2 # 3
    y = M // 2 # 4
    # 상 -> 하
    for i in range(x):
        for j in range(y):
            temp[x+i][j] = arr[i][j]
    # 좌 -> 우
    for i in range(x, N):
        for j in range(y):
            temp[i][y+j] = arr[i][j]
    # 하 -> 상
    for i in range(x, N):
        for j in range(y, M):
            temp[i-x][j] = arr[i][j]
    # 우 -> 좌
    for i in range(x):
        for j in range(y, M):
            temp[i][j-y] = arr[i][j]

    arr = [item[:] for item in temp]


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

seq = list(map(int, input().split()))
for i in seq:
    if i == 1:
        up_down(N, M)
    elif i == 2:
        left_right(N, M)
    # 아래 3과 4의 경우는 행과 열이 바뀌므로(90도회전함) N과 M을 서로 바꿔주어야한다
    # 안그러면 IndexError !
    elif i == 3:
        right_degree_90(N, M)
        N, M = M, N
    elif i == 4:
        left_degree_90(N, M)
        N, M = M, N
    elif i == 5:
        clockwise(N, M)
    else:
        counterclockwise(N, M)
for item in arr:
    print(*item)