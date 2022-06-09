# Baekjoon Online Judge - 2559번. 수열

N, K = map(int, input().split())
dp = list(map(int, input().split()))
# 누적합으로 처음부터 각 자리까지의 합을 넣는다.
for i in range(1, N):
    dp[i] += dp[i - 1]
result = dp[K - 1] # 인덱스가 0부터 시작이므로 K - 1까지가 0부터 K까지의 합이기 때문에 이를 첫 최대값으로 지정
i = 0
# 이후 누적합에서 0번째 인덱스부터 빼주기 시작하면서 최대값을 찾는다.
for j in range(K, N):
    result = max(result, dp[j] - dp[i])
    i += 1
print(result)
