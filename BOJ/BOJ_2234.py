# Baekjoon Online Judge - 2234번. 성곽
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    cnt = 1 # 방 개수
    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            # 범위 체크 
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            # 해당 방을 방문하지 않고 z방향에 따라 벽이 없다면 개수 증가
            if board[x][y][z] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt


# 하우상좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir_values = [8, 4, 2, 1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

# 이진수 표현으로 왼쪽에서부터 8, 4, 2, 1을 통해 값을 만든다. 10이라면 [0, 1, 1, 0]으로 만들어서 다시 해당 위치에 넣음
for i in range(M):
    for j in range(N):
        bits = []
        num = board[i][j]
        for k in dir_values:
            if num >= k:
                bits.append(1)
                num -= k
            else:
                bits.append(0)
        board[i][j] = bits
visited = [[False] * N for _ in range(M)]
result = 0 # 1. 성에 있는 방의 개수
max_len = 0 # 2. 가장 넓은 방의 넓이
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            cnt = bfs(i, j)
            max_len = max(max_len, cnt)
            result += 1
# 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
removed_max_len = max_len
for i in range(M):
    for j in range(N):
        for k in range(4):
            # 해당 위치에서의 방향을 봤을 때 벽이 존재하면 허물고 방의 개수를 체크한다.
            # bfs로 다 돌았다면 다시 벽을 복구해서 체크
            if board[i][j][k] == 1:
                board[i][j][k] = 0
                visited = [[False] * N for _ in range(M)]
                cnt = bfs(i, j)
                board[i][j][k] = 1
                removed_max_len = max(removed_max_len, cnt)
print(result)
print(max_len)
print(removed_max_len)
