# Baekjoon Online Judge - 11051번. 이항 계수 2

N, K = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
# 파스칼의 삼각형에 대한 구현 후 정답 찾음
for i in range(1, N + 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = 1
        elif j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
print(dp[N][K] % 10007)
