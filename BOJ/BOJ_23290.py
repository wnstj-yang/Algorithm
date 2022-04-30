# Baekjoon Online Judge - 23290번. 마법사 상어와 복제


def move_fishes():
    # 새로운 곳에 복제 이유는 물고기가 이동하지 않을 시 계속 반복되기 때문
    temp = [[[] * 4 for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while copy_fishes[x][y]:
                d = copy_fishes[x][y].pop()
                check = True
                for _ in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (s_x, s_y) and smell[nx][ny] == 0:
                        temp[nx][ny].append(d)
                        check = False
                        break
                    d = (d - 1) % 8
                if check:
                    temp[x][y].append(d)
    return temp


def move_shark(sx, sy, cnt, fish_cnt, path):
    global max_cnt, s_x, s_y, s_path
    if cnt == 3:
        if fish_cnt > max_cnt:
            max_cnt = fish_cnt
            s_x, s_y = sx, sy # 상어 좌표 초기화
            s_path = list(path)
        return

    for d in range(4):
        nx = sx + s_dx[d]
        ny = sy + s_dy[d]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        # 방문한 것과 방문안했을 때의 차이는 먹은 물고기의 개수
        if not visited[nx][ny]:
            visited[nx][ny] = True
            move_shark(nx, ny, cnt + 1, fish_cnt + len(copy_fishes[nx][ny]), path + [(nx, ny)])
            visited[nx][ny] = False
        else:
            move_shark(nx, ny, cnt + 1, fish_cnt, path + [(nx, ny)])


def eat_fishes():
    for x, y in s_path:
        if copy_fishes[x][y]:
            copy_fishes[x][y] = []
            smell[x][y] = 3


def remove_smell():
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1


# 문제에 주어진 8방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 상어 상좌하우로 사전순 진행
s_dx = [-1, 0, 1, 0]
s_dy = [0, -1, 0, 1]
M, S = map(int, input().split())
board = [[[] * 4 for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)] # 물고기 냄새 공간
for _ in range(M):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y].append(d - 1)

s_x, s_y = map(int, input().split())
s_x -= 1
s_y -= 1
answer = 0
visited = [[False] * 4 for _ in range(4)]
for _ in range(S):
    # 물고기 공간을 복제한다
    copy_fishes = [[item2[:] for item2 in item] for item in board]
    copy_fishes = move_fishes() # 물고기 이동
    max_cnt = -1
    s_path = [] # 상어 움직이는 좌표
    move_shark(s_x, s_y, 0, 0, [])
    eat_fishes() # 물고기 먹기
    remove_smell() # 냄새 제거
    # 기존의 공간에 복제된 것을 더해줌
    for i in range(4):
        for j in range(4):
            board[i][j] += copy_fishes[i][j]
for i in range(4):
    for j in range(4):
        answer += len(board[i][j])
print(answer)

