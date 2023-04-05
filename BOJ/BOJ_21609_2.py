# Baekjoon Online Judge - 21609번. 상어 중학교

from collections import deque


def gravity():
    for j in range(N):
        cnt = 0
        for i in range(N - 1, -1, -1):
            if board[i][j] == -1:
                cnt = 0
            elif board[i][j] >= 0:
                if cnt != 0:
                    board[i + cnt][j] = board[i][j]
                    board[i][j] = -2
            else:
                cnt += 1


def counter_rotate_90():
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][i] = board[i][N - 1- j]
    return temp


def bfs(x, y):
    color = board[x][y]
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    rainbow_cnt = 0
    rainbows = []
    group_candi = [(color, x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == -1:
                continue
            if not visited[nx][ny]:
                if board[nx][ny] == 0:
                    rainbow_cnt += 1
                    group_candi.append((0, nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    rainbows.append((nx, ny))
                elif board[nx][ny] == color:
                    group_candi.append((color, nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))
    for x, y in rainbows:
        visited[x][y] = False
    group_candi.sort(key=lambda x: (-x[0], x[1], x[2]))

    return group_candi, rainbow_cnt


block_groups = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
while True:
    block_groups = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0:
                group, rainbow_cnt = bfs(i, j)
                if len(group) >= 2:
                    block_groups.append((len(group), rainbow_cnt, group[0][1], group[0][2], group))
    if len(block_groups) == 0:
        break
    block_groups.sort(reverse=True)
    for color, x, y in block_groups[0][4]:
        board[x][y] = -2

    answer += block_groups[0][0] * block_groups[0][0]
    gravity()
    board = counter_rotate_90()
    gravity()

print(answer)
