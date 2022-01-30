# Baekjoon Online Judge - 2407번. 조합

n, m = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = dp[1][0] = dp[1][1] = 1 # 초기설정

for i in range(2, n + 1):
    # 파스칼 삼각형에서 양쪽 끝은 1로 고정
    dp[i][0] = dp[i][i] = 1
    for j in range(1, i):
        # 파스칼 삼각형 형태에서 왼쪽과 오른쪽 위를 더해준다
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][m])

