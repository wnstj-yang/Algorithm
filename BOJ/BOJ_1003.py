# Baekjoon Online Judge - 1003번. 피보나치 함수

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * (N + 2)
    dp[0], dp[1] = 0, 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # 0 호출횟수는 구하려는 피보나치 수의 이전, 1은 구하려는 수와 같다
    print(dp[N - 1], dp[N])
