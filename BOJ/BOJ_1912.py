# Baekjoon Online Judge - 1912번. 연속합

N = int(input())
dp = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    # 현재 값이랑 이전까지 합한 것들이랑 비교해서 작으면 그대로 현재 값이 넘어감
    if dp[i] < dp[i - 1] + dp[i]:
        dp[i] += dp[i - 1]
print(max(dp[1:]))
