# Baekjoon Online Judge - 14925번. 목장 건설하기
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
L = 0
dp = [[1] * N for _ in range(M)]
# 가로 혹은 세로가 1일 때 최대가 1이므로 따로 예외처리 진행
if M == 1 or N == 1:
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 0:
                L = 1

for i in range(1, M):
    for j in range(1, N):
        # 현재 위치가 0이고 위, 왼쪽 대각선, 왼쪽에 똑같이 0인 경우 dp테이블안에 최소값에 1을 더한 것이 정사각형의 크기가 된다.
        if arr[i][j] == 0:
            if arr[i - 1][j] == 0 and arr[i][j - 1] == 0 and arr[i - 1][j - 1] == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            L = max(L, dp[i][j])

print(L)
