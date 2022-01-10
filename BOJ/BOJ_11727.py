# Baekjoon Online Judge - 11727번. 2xn 타일링 2

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
# 각각 점화식을 세웠을 때 n이 3부터 1번, 2번째 이전의 값에 2를 곱하고 더한 값이 경우의 수를 나타내는 규칙이 존재한다
for i in range(3, n + 1):
    dp[i] = dp[i-1] + 2 * dp[i-2]
print(dp[n] % 10007)
