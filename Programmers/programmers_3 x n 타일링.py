def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[2] = 3 # 총 3가지의 조합이 존재
    prev = 0
    # 홀수는 0, 짝수는 이전 크기에 길이가 2가 붙으므로 3가지의 조합이 있어서 3을 곱해준다.
    # 예시에서처럼 다르게 만들어지는 경우의 수가 2개가 있는데 이를 그 이전의 값과 2를 곱해주고 현재의 값에 2를 더해준다
    # dp[i] = dp[i - 2] * 3 + (dp[i - 4] + dp[i - 6] + dp[i - 8]...) * 2 + 2
    for i in range(4, n + 1, 2):
        prev += dp[i - 4] * 2
        dp[i] = (dp[i - 2] * 3 + prev + 2) % 1000000007
    answer = dp[n]
    return answer
