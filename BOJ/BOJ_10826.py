# Baekjoon online Judge - 10826번. 피보나치 수 4

N = int(input())
dp = [0] * 10001
dp[0], dp[1] = 0, 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[N])
