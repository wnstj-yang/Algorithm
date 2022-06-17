# Baekjoon Online Judge - 19236번. 청소년 상어


def dfs(x, y, result, board):
    global answer
    result += board[x][y][0]
    answer = max(result, answer)
    board[x][y][0] = 0 # 물고기 먹음
    # 1. 물고기의 번호 순서에 따라 이동
    for n in range(1, 17):
        check = False
        for i in range(4):
            for j in range(4):
                # 번호 순서대로 진행하므로 해당 번호를 찾은 후 방향에 따라 이동이 가능한지 파악한다.
                if board[i][j][0] == n:
                    check = True
                    d = board[i][j][1]
                    for k in range(8):
                        nd = (d + k) % 8
                        nx = i + dx[nd]
                        ny = j + dy[nd]
                        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == x and ny == y):
                            continue
                        board[i][j][1] = nd
                        board[nx][ny], board[i][j] = board[i][j], board[nx][ny]
                        break
                # check를 통해 해당 번호를 방문하면 그 다음 물고기의 이동을 시작한다.
                if check:
                    break
            if check:
                break

    s_d = board[x][y][1] # 상어 방향
    # 2. 상어 방향에 따라 dfs로 먹이를 먹으면서 최대 값을 구한다.
    for k in range(1, 5):
        # 상어의 방향에 따라 여러 개의 공간에 이동이 가능하므로 k만큼 곱해서 진행
        sx = x + dx[s_d] * k
        sy = y + dy[s_d] * k
        if sx < 0 or sx >= 4 or sy < 0 or sy >= 4 or board[sx][sy][0] == 0:
            continue
        # 리스트 슬라이싱 시 copy 보다 빠르게 접근 가능
        temp = [[item[:] for item in board[k]] for k in range(4)]
        dfs(sx, sy, result, temp)


# 첫 위부터 시계방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
board = [[] for _ in range(4)]
answer = 0
for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        board[i].append([info[2 * j], info[2 * j + 1] - 1])

dfs(0, 0, 0, board)
print(answer)
