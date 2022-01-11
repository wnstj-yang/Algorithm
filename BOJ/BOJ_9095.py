# Baekjoon Online Judge - 9095번. 1, 2, 3 더하기

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [0] * 11
    dp[1], dp[2], dp[3] = 1, 2, 4
    # 4번째부터 1~3번째들의 수를 합한 것이 경우의 수로 나타나는 규칙
    for i in range(4, n + 1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])
