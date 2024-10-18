from collections import deque

def solution(board):
    board = [list(item) for item in board]
    answer = -1
    n, m = len(board), len(board[0])
    sx, sy = -1, -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                sx, sy = i, j
                break
        if not (sx == -1 and sy == -1):
            break
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    # print(sx, sy)
    while q:
        x, y, cnt = q.popleft()
        # print(x, y, cnt)
        if board[x][y] == 'G':
            answer = cnt
            break
        for k in range(4):
            tx, ty = x, y
            while True:
                nx = tx + dx[k]
                ny = ty + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 'D':
                    if visited[tx][ty]:
                        break
                    visited[tx][ty] = True
                    q.append((tx, ty, cnt + 1))
                    break
                tx, ty = nx, ny
    return answer