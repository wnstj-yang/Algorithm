# Baekjoon Online Judge - 14495번. 피보나치 비스무리한 수열

n = int(input())
dp = [0] * 117
dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 3]
print(dp[n])
