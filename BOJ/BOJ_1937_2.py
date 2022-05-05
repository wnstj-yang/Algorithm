# Baekjoon Online Judge - 1937번. 욕심쟁이 판다 - DFS + DP
# python3으로는 Recursionerror발생. pypy3으로는 통과
# 그래서 python3으로 통과 시 sys.setrecursionlimit(10**6) 설정해야함

def dfs(x, y):
    # 방문한 적이 있을 시 해당 값(거리) 반환
    if dp[x][y] != 0:
        return dp[x][y]

    dp[x][y] = 1 # 첫 방문 시 1로 초기화
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        # 움직일 수 있는 칸일 때
        if board[nx][ny] > board[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1) # 가장 많이 이동할 수 있는 칸으로 초기화
    # 다 돌고난 이후
    return dp[x][y]


N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        result = dfs(i, j)
        answer = max(answer, result)
print(answer)
