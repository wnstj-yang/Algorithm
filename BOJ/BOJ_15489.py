# Baekjoon Online Judge - 15489번. 파스칼 삼각형

R, C, W = map(int, input().split())
dp = [[0] * 31 for _ in range(31)]
dp[1][0] = 1
result = 0
for i in range(2, 31):
    for j in range(i):
        if j == 0 or j == i - 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

idx = 1
C -= 1
for i in range(R, R + W):
    for j in range(C, C + idx):
        result += dp[i][j]
    idx += 1
print(result)
