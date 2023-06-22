# 다이내믹 프로그래밍 - 217p. 1로 만들기

x = int(input())

dp = [0] * 30001

for i in range(2, x + 1):
    # i에서 1을 뺀 경우 (이전과의 값과 1을 뺀 경우 1을 더해준다)
    # 비교군이 필요하기 때문에 다른 것은 나누지만 해당 부분은 더하기 때문에 기준으로 삼는다
    dp[i] = dp[i - 1] + 1
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[:x])
