# Baekjoon Online Judge - 1463번. 1로 만들기

X = int(input())

dp = [0] * (X + 1)

for i in range(2, X + 1):
    # dp안에는 사용하는 횟수의 최솟값 존재. 조건 3. "1을 뺀다" => 횟수 1 증가
    dp[i] = dp[i - 1] + 1
    # 조건 1. 3으로 나누어 떨어지면 3으로 나눈다( 1 증가는 횟수임 )
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # 조건 2. 2로 나누어 떨어지면 2로 나눈다
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[X])
