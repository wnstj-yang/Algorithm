# Baekjoon Online Judge - 2839번. 설탕 배달

# DP
N = int(input())
dp = [5001] * (N + 3) # N보다 1 큰 값을 지정. 적절히 값을 크게 줬다.
dp[3] = dp[5] = 1
for i in range(6, N + 1):
    # 점화식 세웠을 때 i-3번째 혹은 i-5번째의 최소값에서 + 1을 해주면 된다.
    dp[i] = min(dp[i-3], dp[i-5]) + 1
if dp[N] >= 5001:
    print(-1)
else:
    print(dp[N])
