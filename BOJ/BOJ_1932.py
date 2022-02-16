# Baekjoon Online Judge - 1932번. 정수 삼각형

N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(len(dp[i])):
        # 첫 번째는 이전의 첫번째 값의 합
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i - 1][j]
        # 마지막 번째는 마지막 값의 합 
        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
        # 이외의 경우 파스칼 삼각형의 역 방식으로 현재 위치에서 왼쪽, 오른쪽 대각선의 합 중 최대값을 넣는다
        else:
            dp[i][j] = max(dp[i][j] + dp[i - 1][j - 1], dp[i][j] + dp[i - 1][j])
print(max(dp[N - 1]))
