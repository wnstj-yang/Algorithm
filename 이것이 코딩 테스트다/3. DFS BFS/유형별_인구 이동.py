# DFS/BFS - 유형별 문제 353p - 인구 이동

from collections import deque


def search_land(x, y, p, num):
    q = deque()
    q_val = p
    length = 1
    q.append((x, y, p))
    visited[x][y] = num

    while q:
        x, y, p = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            diff = abs(p - board[nx][ny])
            if visited[nx][ny] == 0 and L <= diff <= R:
                visited[nx][ny] = num
                q.append((nx, ny, board[nx][ny]))
                q_val += board[nx][ny]
                length += 1
    num_values[num] = q_val // length


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0
while True:
    num = 1
    visited = [[0] * N for _ in range(N)]
    num_values = {}
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                search_land(i, j, board[i][j], num)
                num += 1
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = num_values[visited[i][j]]
    if board == result:
        print(time)
        break
    else:
        board = result
        time += 1
