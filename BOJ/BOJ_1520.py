# Baekoon Online Judge - 1520번. 내리막 길


def dfs(x, y):
    # 도착지점에 왔으면 경로 하나로 인정되니 1 반환
    if x == M - 1 and y == N - 1:
        return 1
    
    # 이미 방문한 곳이므로 더 이상 탐색 필요 X
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0 # 경로 탐색 중 방문 표시
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if board[x][y] > board[nx][ny]:
            # 조건에 맞을 시 경로에 속하는 지점들과의 합을 구함
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0)
print(dp[0][0])
