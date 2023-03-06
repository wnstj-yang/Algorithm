# DFS/BFS - 유형별 문제. 연구소 341p

from collections import deque


def combi(idx, k):
    global ans
    if k == 3:
        result = check()
        ans = max(ans, result)
        return

    for i in range(idx, len(candis)):
        if not visited[i]:
            visited[i] = True
            candi[k] = i
            combi(i, k + 1)
            visited[i] = False


def check():
    arr = [item[:] for item in board]
    for i in candi:
        x, y = candis[i]
        arr[x][y] = 1
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx, ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
    return cnt


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
candis = []
virus = deque()
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            candis.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))
candi = [0] * 3
visited = [False] * len(candis)
combi(0, 0)
print(ans)