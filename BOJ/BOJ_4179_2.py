# Baekjoon Online Judge - 4179번. - 2번째

from collections import deque


def spread_fires():
    temp = deque()
    while fires:
        x, y = fires.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if not visited[nx][ny] and board[nx][ny] != '#':
                board[nx][ny] = 'F'
                temp.append((nx, ny))
                visited[nx][ny] = True
    return temp


def check():
    global answer
    temp = deque()
    while j_coors:
        x, y, time = j_coors.popleft()
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            answer = time
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if board[nx][ny] == '.':
                board[nx][ny] = 'J'
                temp.append((nx, ny, time + 1))
    return temp


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
# 1. 불을 먼저 퍼트린다
# 2. 지훈이가 움직일 수 있는 공간이 있다면 움직이고 아니면 IMPOSSIBLE
fires = deque()
j_coors = deque()
answer = 987654321

for i in range(R):
    for j in range(C):
        if board[i][j] == 'F':
            visited[i][j] = True
            fires.append((i, j))
        elif board[i][j] == 'J':
            j_coors.append((i, j, 1))

while True:
    fires = spread_fires()
    j_coors = check()
    if answer != 987654321:
        print(answer)
        break

    if len(j_coors) == 0:
        print('IMPOSSIBLE')
        break

