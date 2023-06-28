# 다이내믹 프로그래밍 - 금광 375p

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = []
    idx = 0
    result = 0
    for i in range(N):
        dp.append(arr[idx:idx+M])
        idx += M
    # 맨위, 맨 아래 그 외 기준으로 3가지를 남기고
    # 왼쪽에서부터 오른쪽을 보는 것이 아니라 오른쪽에서부터 왼쪽을 본다
    # 왼쪽에서부터 오른쪽을 본다면 배열을 하나 더 만들어서 번거롭게 다시 점검해야하므로
    # 오른쪽에서부터 왼쪽을 보아서 거꾸로 진행을 한다.
    for j in range(1, M):
        for i in range(N):
            if i == 0:
                dp[i][j] = dp[i][j] + max(dp[i][j - 1], dp[i + 1][j - 1])
            elif i == N - 1:
                dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
    for i in dp:
        result = max(i)
    print(result)
