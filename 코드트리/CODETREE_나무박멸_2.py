# 코드트리 - 나무박멸

from collections import deque


# 1. 인접나무 증가
def increase_trees():
    for i in range(N):
        for j in range(N):
            if herbicide_state[i][j] == 0 and board[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if herbicide_state[nx][ny] == 0 and board[nx][ny] > 0:
                        cnt += 1
                board[i][j] += cnt

# 2.
def spread_trees():
    coors = []
    for i in range(N):
        for j in range(N):
            if herbicide_state[i][j] == 0 and board[i][j] > 0:
                temp = []
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if herbicide_state[nx][ny] == 0 and board[nx][ny] == 0:
                        cnt += 1
                        temp.append((nx, ny))

                for x, y in temp:
                    coors.append((x, y, board[i][j] // cnt))
    for x, y, cnt in coors:
        board[x][y] += cnt


# 3.
def spread_herbicide():
    global result
    x, y = 0, 0
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if herbicide_state[i][j] == 0 and board[i][j] > 0:
                cnt = board[i][j]
                for k in range(4, 8):
                    length = 1
                    while length <= K:
                        nx = i + dx[k] * length
                        ny = j + dy[k] * length
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            break
                        if board[nx][ny] <= 0 or herbicide_state[nx][ny] != 0:
                            break
                        cnt += board[nx][ny]
                        length += 1
                if max_cnt < cnt:
                    x, y = i, j
                    max_cnt = cnt
    result += max_cnt
    board[x][y] = 0
    herbicide_state[x][y] = C
    for k in range(4, 8):
        length = 1
        while length <= K:
            nx = x + dx[k] * length
            ny = y + dy[k] * length
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                break

            herbicide_state[nx][ny] = C
            if board[nx][ny] <= 0:
                break
            board[nx][ny] = 0
            length += 1


def decrease_herbicide():
    for i in range(N):
        for j in range(N):
            if herbicide_state[i][j] > 0:
                herbicide_state[i][j] -= 1


N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
herbicide_state = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
result = 0

for _ in range(M):
    increase_trees()
    spread_trees()
    decrease_herbicide()
    spread_herbicide()

print(result)