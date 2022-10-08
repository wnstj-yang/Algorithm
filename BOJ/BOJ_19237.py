# Baekjoon Online Judge - 19237번. 어른 상어


# 냄새 갱신 ( 기존에 있으면 1 차감, 상어가 위치한 곳이라면 새로운 냄새 부여 )
def update_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

            if board[i][j] != 0:
                smell[i][j][0] = board[i][j]
                smell[i][j][1] = k


# 상어 방향 설정 및 이동하기
def move():
    # 기존의 board에서 움직이고 닫을 경우 중간에 맞지 않는 경우가 생김
    # 새로운 board를 만들어 갱신
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                moved = False
                shark = board[i][j]
                # 현재 방향인 상태에서 주변 파악 후 움직일 수 있는 유무
                for z in priorities[shark - 1][directions[shark - 1] - 1]:
                    nx = i + dx[z]
                    ny = j + dy[z]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    # 냄새가 있지 않은 곳. 즉, 움직일 수 있다면 상어를 움직이고 기존 위치는 0으로 표시
                    # 냄새가 있다면 해당 위치의 상어의 최소값을 가진 번호만 살아 남긴다. 그외 상어는 0으로 다시 표시
                    if smell[nx][ny][1] == 0:
                        directions[shark - 1] = z
                        if new_board[nx][ny] == 0:
                            new_board[nx][ny] = shark
                        else:
                            new_board[nx][ny] = min(new_board[nx][ny], shark)
                        moved = True
                        break

                # 4방향에 돌아도 움직이지 못하는 경우 자신의 냄새가 있는 곳으로 이동
                if not moved:
                    for z in priorities[shark - 1][directions[shark - 1] - 1]:
                        nx = i + dx[z]
                        ny = j + dy[z]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue

                        # 냄새나는 곳이 현재 상어가 남긴 곳과 같을 때 움직인다.
                        if smell[nx][ny][0] == shark:
                            directions[shark - 1] = z
                            new_board[nx][ny] = shark
                            break

    return new_board


N, M, k = map(int, input().split())

# 상하좌우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

board = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))

priorities = []
for _ in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

smell = [[[0, 0] for _ in range(N)] for _ in range(N)]

time = 1
while True:
    update_smell()
    board = move()
    cnt = 0
    only_one = True
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                cnt += 1
            if cnt > 1:
                only_one = False
                break
        if not only_one:
            break
    if only_one:
        print(time)
        break
    else:
        time += 1
    if time > 1000 and cnt > 1:
        print(-1)
        break
