# SW Expert Academy - 11315번. 오목 판정


def check():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for k in range(4):
                    x, y = i, j
                    flag = True
                    for _ in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            flag = False
                            break
                        if board[nx][ny] != 'o':
                            flag = False
                            break
                        x, y = nx, ny
                    if flag:
                        return 'YES'
    return 'NO'


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]
    print('#{} {}'.format(tc, check()))


