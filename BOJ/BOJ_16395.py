# Baekjoon Online Judge - 16395번. 파스칼의 삼각형

dp = [[0] * 31 for _ in range(31)]
dp[1][0] = 1
for i in range(2, 31):
    for j in range(i):
        if j == 0 or j + 1 == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
N, K = map(int, input().split())
print(dp[N][K - 1])
