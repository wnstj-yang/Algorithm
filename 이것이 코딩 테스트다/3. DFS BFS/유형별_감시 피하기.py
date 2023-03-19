# DFS/BFS - 유형별. 351p 감시 피하기

from itertools import combinations


def search(x, y, i):
    cnt = 1
    while True:
        nx = x + dx[i] * cnt
        ny = y + dy[i] * cnt
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 'O':
            return False
        if board[nx][ny] == 'S':
            return True
        cnt += 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty_spots = []
teachers = []
N = int(input())
board = [list(map(str, input().split())) for _ in range(N)]
answer = 'NO'
for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            empty_spots.append((i, j))
        elif board[i][j] == 'T':
            teachers.append((i, j))
for obstacles in combinations(empty_spots, 3):
    for x, y in obstacles:
        board[x][y] = 'O'
    isBlocked = False
    for x, y in teachers:
        for i in range(4):
            if search(x, y, i):
                isBlocked = True
                break
        if isBlocked:
            break

    if not isBlocked:
        answer = 'YES'
        break
    for x, y in obstacles:
        board[x][y] = 'X'
print(answer)