# Baekjoon Online Judge - 1915번. 가장 큰 정사각형

n, m = map(int, input().split())
dp = [[0] * m for _ in range(n)]
arr = [list(map(int, input())) for _ in range(n)]
result = 0
# (1,1)부터 시작해서 현재 위치의 값이 1인 경우 왼쪽 대각선, 왼쪽, 위 내용 중 최소값에서 1을 더해 값을 저장한다.
# 즉, 만들어질 수 있는 정사각형의 크기인 n을 dp로 구현
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        elif arr[i][j] == 1:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    result = max(result, max(dp[i]))

print(result ** 2)
