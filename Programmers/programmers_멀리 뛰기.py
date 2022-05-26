def solution(n):
    answer = 0
    dp = [0] * 2001
    dp[1], dp[2] = 1, 2
    # 값이 클 경우 메모리 초과가 가능하므로 미리 나머지연산
    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
    answer = dp[n]
    return answer
