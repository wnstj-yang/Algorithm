# Baekjoon Online Judge - 1010번. 다리 놓기
# DP 이용

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1:
                dp[i][j] = j
                continue
            if i == j:
                dp[i][j] = 1
            else:
                # 일종의 파스칼 삼각형 형태이다.
                if i < j:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[N][M])