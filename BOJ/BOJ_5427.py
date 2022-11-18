# Baekjoon Online Judge - 5427번. 불

from collections import deque


def spread_fire():
    temp = deque()
    while fires:
        x, y = fires.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if board[nx][ny] == '.' or board[nx][ny] == '@':
                temp.append((nx, ny))
                board[nx][ny] = '*'
    return temp


def move():
    global moving
    temp = deque()
    is_escape = False
    result = 0
    while moving:
        x, y, time = moving.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                is_escape = True
                result = time
                break
            if not visited[nx][ny] and board[nx][ny] == '.':
                visited[nx][ny] = True
                temp.append((nx, ny, time + 1))

        if is_escape:
            break
    if is_escape:
        return result
    else:
        moving = temp
        if len(moving) == 0:
            return False
        return 'keep'


T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    fires = deque()
    moving = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fires.append((i, j))
            elif board[i][j] == '@':
                moving.append((i, j, 1))
                visited[i][j] = True
    while True:
        fires = spread_fire()
        value = move()
        if value == 'keep':
            continue
        elif value:
            print(value)
            break
        else:
            print('IMPOSSIBLE')
            break
