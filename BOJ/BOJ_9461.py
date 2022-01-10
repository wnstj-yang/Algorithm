# Baekjoon Online Judge - 9461번. 파도반 수열

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * 101
    dp[1], dp[2], dp[3] = 1, 1, 1
    # 인덱스상으로 4번째부터는 두, 세번째 이전의 값들을 더한 것이 들어가는 규칙이 존재한다
    for i in range(4, N + 1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[N])
