# SW Expert Academy - 5650번. [모의 SW 역량테스트] 핀볼 게임

def search(x, y, dir):
    st_x, st_y = x, y
    cnt = 0
    while True:
        x = x + dx[dir]
        y = y + dy[dir]
        if x < 0 or x >= N or y < 0 or y >= N:
            dir = (dir + 2) % 4
            cnt += 1
            continue

        if (x == st_x and y == st_y) or board[x][y] == -1:
            return cnt

        if 1 <= board[x][y] <= 5:
            dir = blocks[board[x][y]][dir]
            cnt += 1

        elif 6 <= board[x][y] <= 10:
            for wx, wy in wormholes[board[x][y]]:
                if wx != x or wy != y:
                    x, y = wx, wy
                    break


# 상좌하우 0123
blocks = {
    1: (2, 0, 3, 1), 2: (3, 2, 0, 1), 3: (1, 3, 0, 2),
    4: (2, 3, 1, 0), 5: (2, 3, 0, 1)
}


T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    wormholes = {}
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 6:
                if board[i][j] not in wormholes:
                    wormholes[board[i][j]] = [(i, j)]
                else:
                    wormholes[board[i][j]].append((i, j))

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    result = search(i, j, k)
                    answer = max(result, answer)

    print('#{} {}'.format(tc, answer))
