# Baekjoon Online Judge - 1890번. 점프
# 수학 배울 때 최단거리 구하는 방식과 유사

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        # 오른쪽으로 갈 수 있을 때
        if j + board[i][j] < N:
            dp[i][j + board[i][j]] += dp[i][j]
        # 아래로 갈 수 있을 때
        if i + board[i][j] < N:
            dp[i + board[i][j]][j] += dp[i][j]
print(dp[N - 1][N - 1])
