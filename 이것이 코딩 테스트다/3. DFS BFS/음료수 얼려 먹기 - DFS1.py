# 149~150p 실전 문제
# DFS 방법 형태 첫번째

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not visited[nx][ny] and board[nx][ny] == 0:
            visited[nx][ny] = True
            dfs(nx, ny)


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == 0:
            dfs(i, j)
            result += 1
print(result)

# 예제 - 1
# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력 - 1
# 3

# 예제 - 2
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
# 출력 - 2
# 8