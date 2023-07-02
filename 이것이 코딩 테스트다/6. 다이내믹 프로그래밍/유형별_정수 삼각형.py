# 다이내믹 프로그래밍 - 정수 삼각형, 376p


N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]
max_val = dp[0][0] # 삼각형의 맨 처음 값
for i in range(1, N):
    for j in range(i + 1):
        # 삼각형의 줄 첫번째 값인 경우에는 대각선 오른쪽 위만 가능 
        if j == 0:
            dp[i][j] = max(dp[i][j], dp[i][j] + dp[i - 1][j])
        # 맨 끝의 경우 대각선 왼쪽 위만 가능
        elif j == i:
            dp[i][j] = max(dp[i][j], dp[i][j] + dp[i - 1][j - 1])
        # 그 외의 경우 왼쪽, 오른쪽 위 대각선과 현재 값을 더해 최대 값을 저장
        else:
            dp[i][j] = max(dp[i][j] + dp[i - 1][j - 1], dp[i][j] + dp[i - 1][j])
        max_val = max(max_val, dp[i][j]) # 각 값들을 순회하면서 최대 값 구하기

print(max_val)
