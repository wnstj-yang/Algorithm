# CODETREE 2022 상반기 오후 2번 - 나무박멸


def grow_trees():
    for i in range(N):
        for j in range(N):
            # 제초제가 뿌려져 있지않고 나무가 있는 공간이라면
            if board[i][j] > 0 and dopping[i][j] == 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if board[nx][ny] > 0 and dopping[nx][ny] == 0:
                        cnt += 1
                board[i][j] += cnt


def spread_trees():
    coors = []
    # 새로운 리스트를 만들어서 갱신시켜도 무방
    # new_trees = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and dopping[i][j] == 0:
                temp = []
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    # 제초제, 다른 나무, 벽 모두 없을 때 번식 가능
                    if board[nx][ny] == 0 and dopping[nx][ny] == 0:
                        cnt += 1
                        temp.append((nx, ny))
                for x, y in temp:
                    # new_trees[x][y] += board[i][j] // cnt
                    coors.append((x, y, board[i][j] // cnt))
    # for i in range(N):
    #     for j in range(N):
    #         board[i][j] += new_trees[i][j]
    for x, y, cnt in coors:
        board[x][y] += cnt


def search_spread():
    global result
    x, y = 0, 0
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and dopping[i][j] == 0:
                cnt = board[i][j]
                for k in range(4):
                    length = 1
                    while length <= K:
                        nx = i + diagx[k] * length
                        ny = j + diagy[k] * length
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            break
                        if board[nx][ny] <= 0 or dopping[nx][ny] != 0:
                            break
                        length += 1
                        cnt += board[nx][ny]
                if max_cnt < cnt:
                    x, y = i, j
                    max_cnt = cnt
    result += max_cnt
    if board[x][y] == -1:
        return 0

    return spread_dopping(x, y)


def spread_dopping(x, y):
    dopping[x][y] = C
    board[x][y] = 0 # 제초제를 뿌리기 때문에 0으로 초기화
    for i in range(4):
        length = 1
        while length <= K:
            nx = x + diagx[i] * length
            ny = y + diagy[i] * length
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                break
            dopping[nx][ny] = C
            if board[nx][ny] <= 0:
                break
            board[nx][ny] = 0
            length += 1


def decrease_dopping():
    for i in range(N):
        for j in range(N):
            if dopping[i][j] > 0:
                dopping[i][j] -= 1


N, M, K, C = map(int, input().split())
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 대각선
diagx = [-1, -1, 1, 1]
diagy = [-1, 1, 1, -1]
board = [list(map(int, input().split())) for _ in range(N)]
dopping = [[0] * N for _ in range(N)]
result = 0
for _ in range(M):
    grow_trees()
    spread_trees()
    # c년만큼 제초제가 남아있다가 'c + 1년째'가 될 때 사라지게 된다.
    decrease_dopping()
    search_spread()
print(result)
