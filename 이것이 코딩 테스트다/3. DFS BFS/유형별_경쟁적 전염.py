# DFS/BFS - 유형별. 경쟁적 전염 344p

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
S, X, Y = map(int, input().split())
q = []
for x in range(N):
    for y in range(N):
        if board[x][y] != 0:
            q.append((x, y, board[x][y]))
            visited[x][y] = True
q.sort(key=lambda x: x[2])

while S:
    temp = []
    while q:
        x, y, num = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if not visited[nx][ny] and board[nx][ny] == 0:
                board[nx][ny] = num
                visited[nx][ny] = True
                temp.append((nx, ny, num))
    temp.sort(key=lambda x: x[2])
    q = temp
    S -= 1
print(board[X - 1][Y - 1])
