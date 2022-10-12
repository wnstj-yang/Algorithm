# CODETREE 2022 상반기 오전 1번 - 술래 잡기


def change_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2


def move_robbers(c_x, c_y):
    temp = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                length = len(board[i][j])
                # 나무만 있는 곳이면 넘어간다
                if abs(c_x - i) + abs(c_y - j) <= 3:
                    # 나무가 존재하면
                    if board[i][j][0] == 4:
                        # 나무가 존재하며 도망자가 1명이상 있는 경우 나무제외 도망자들을 움직인다.
                        if length > 1:
                            while board[i][j][1:]:
                                d = board[i][j].pop()
                                nx = i + dx[d]
                                ny = j + dy[d]
                                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                                    d = change_direction(d)
                                    nx = i + dx[d]
                                    ny = j + dy[d]
                                if nx == c_x and ny == c_y:
                                    temp.append((i, j, d))
                                else:
                                    temp.append((nx, ny, d))
                    # 나무가 존재하지 않는 경우라면 그냥 진행
                    else:
                        while board[i][j]:
                            d = board[i][j].pop()
                            nx = i + dx[d]
                            ny = j + dy[d]
                            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                                d = change_direction(d)
                                nx = i + dx[d]
                                ny = j + dy[d]
                            if nx == c_x and ny == c_y:
                                temp.append((i, j, d))
                            else:
                                temp.append((nx, ny, d))
    while temp:
        x, y, d = temp.pop()
        board[x][y].append(d)


def move_chaser(c_x, c_y, chaser_d, m_cnt, cnt, times, go_back, k):
    # c_x, c_y : chaser의 좌표
    # chaser_d : chaser의 방향
    # m_cnt, cnt : m_cnt는 움직이는 길이, cnt는 m_cnt만큼 가는지 확인
    # times : 회전 할 때마다 몇 번 돌아야 하는지 확인해준다 ( 마지막(N - 1)은 3번, 나머지는 2번)
    # go_back : 달팽이 방향인지 역달팽이 방향인지 확인
    # k : k는 도망자들을 찾을 때 턴 수를 의미
    if go_back:
        if m_cnt == N - 1:
            if times < 3:
                c_x = c_x + go_dx[chaser_d]
                c_y = c_y + go_dy[chaser_d]
                cnt += 1
                if cnt == m_cnt:
                    chaser_d = (chaser_d + 1) % 4
                    cnt = 0
                    times += 1

                if times == 3:
                    chaser_d = 0
                    times = 0
                    go_back = False
                seek(c_x, c_y, chaser_d, k)
        else:
            if times < 2:
                c_x = c_x + go_dx[chaser_d]
                c_y = c_y + go_dy[chaser_d]
                cnt += 1
                if cnt == m_cnt:
                    chaser_d = (chaser_d + 1) % 4
                    cnt = 0
                    times += 1

                if times == 2:
                    times = 0
                    m_cnt += 1
                seek(c_x, c_y, chaser_d, k)

    else:
        if m_cnt == N - 1:
            if times < 3:
                c_x = c_x + back_dx[chaser_d]
                c_y = c_y + back_dy[chaser_d]
                cnt += 1
                if cnt == m_cnt:
                    chaser_d = (chaser_d + 1) % 4
                    cnt = 0
                    times += 1

                if times == 3:
                    m_cnt -= 1
                    times = 0
                seek(c_x, c_y, chaser_d, k)
        else:
            if times < 2:
                c_x = c_x + back_dx[chaser_d]
                c_y = c_y + back_dy[chaser_d]
                cnt += 1
                if cnt == m_cnt:
                    chaser_d = (chaser_d + 1) % 4
                    cnt = 0
                    times += 1
                if times == 2:
                    times = 0
                    m_cnt -= 1
                    if m_cnt == 0:
                        chaser_d = 0
                        go_back = True
                seek(c_x, c_y, chaser_d, k)
    return [c_x, c_y, chaser_d, m_cnt, cnt, times, go_back]


def seek(c_x, c_y, d, k):
    global result
    dist = 0
    cnt = 0
    robbers = 0
    # 현재 위치를 포함하여 거리가 3까지의 달팽이, 역달팽이 방향에 따라 진행하고, 나무가 없는 곳일 때 도망자들을 모두 잡는다.
    while dist < 3:
        if go_back:
            nx = c_x + go_dx[d] * cnt
            ny = c_y + go_dy[d] * cnt
        else:
            nx = c_x + back_dx[d] * cnt
            ny = c_y + back_dy[d] * cnt
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break
        if board[nx][ny]:
            if board[nx][ny][0] == 4:
                dist += 1
                cnt += 1
                continue
            else:
                robbers += len(board[nx][ny])
                while board[nx][ny]:
                    board[nx][ny].pop()
        dist += 1
        cnt += 1
    result += robbers * k


N, M, H, K = map(int, input().split())
# 상우하좌 달팽이
go_dx = [-1, 0, 1, 0]
go_dy = [0, 1, 0, -1]
# 하우상좌 역달팽이
back_dx = [1, 0, -1, 0]
back_dy = [0, 1, 0, -1]
# 상하좌우 => 0, 1, 2, 3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [[[] for _ in range(N)] for _ in range(N)]
result = 0
times = 0
c_x, c_y = N // 2, N // 2 # chaser 좌표
chaser_d = 0 # chaser의 방향
go_back = True # True면 달팽이 방향, False면 역달팽이
m_cnt = 1 # 달팽이로 돌면서
cnt = 0 # 이동 횟수(m_cnt)

for _ in range(M):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    # d = 1이면 좌우, d = 2면 상하 / 첫 시작은 좌우면 오른쪽, 상하는 아래
    if d == 1:
        board[x][y].append(3)
    else:
        board[x][y].append(1)

# 나무가 있는 곳은 맨 앞에 나무를 놔서 도망자가 숨을 수 있는지 파악
for _ in range(H):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y].append(4)
    board[x][y].sort(reverse=True)

for k in range(1, K + 1):
    move_robbers(c_x, c_y)
    c_x, c_y, chaser_d, m_cnt, cnt, times, go_back = move_chaser(c_x, c_y, chaser_d, m_cnt, cnt, times, go_back, k)


print(result)
