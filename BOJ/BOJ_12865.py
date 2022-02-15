# Baekjoon Online Judge - 12865번. 평범한 배낭

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
backage_info = []
for _ in range(N):
    W, V = map(int, input().split())
    backage_info.append((W, V))
for i in range(1, N + 1):
    w, v = backage_info[i - 1] # 주어진 순서에 따른 물건의 무게와 가치
    for j in range(1, K + 1):
        # 현재 물건의 무게보다 적용 가능한 무게가 작다면 이전 물건까지의 값을 넣어준다
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 현재 물건의 무게보다 적용 가능한 무게가 크거나 같으면
        # 1. 무게를 빼서 현재 물건의 가치와 더한 값 a => v(현재 가치) + dp[i - 1][j - w] (이전 물건 까지의 가치와 현재 무게를 뺀 가치 합산)
        # 2. 이전 물건까지의 가치와 현재와 비교한 값 b => dp[i - 1][j]
        # 1, 2와의 비교를 통해 최대 값을 저장해야함
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])
print(dp[N][K])
