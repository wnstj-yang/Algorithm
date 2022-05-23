# Baekjoon Online Judge - 7579번. 앱

N, M = map(int, input().split())
active = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
_sum = sum(costs)
result = _sum
dp = [[0] * (result + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    byte = active[i]
    cost = costs[i]
    for j in range(1, _sum + 1):
        # 비용이 적은 경우 비활성화를 못하므로 이전까지의 활성, 비활성화된 상태에서의 바이트 수를 받는다
        if j < cost:
            dp[i][j] = dp[i - 1][j]
        # 비용이 이상인 경우 현재 바이트 수와 현재의 비용을 뺀 이전까지 진행했던 비활성화된 상태의 값과 이전까지 진행했던 값과의 최대값
        else:
            dp[i][j] = max(byte + dp[i - 1][j - cost], dp[i - 1][j])
        # M바이트 이상인 경우 비용의 최소값을 구한다.
        if dp[i][j] >= M:
            result = min(result, j)
print(result)

