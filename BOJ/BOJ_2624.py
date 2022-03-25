# Baekjoon Online Judge - 2624번. 동전 바꿔주기

T = int(input())
k = int(input())
# 행은 동전의 가지 수 열은 금액을 나타낸다
dp = [[0] * (T + 1) for _ in range(k + 1)]
dp[0][0] = 1 # 동전과 금액의 수가 같을 때 하나의 경우의 수로 표현
for i in range(1, k + 1):
    p, n = map(int, input().split())
    dp[i][0] = dp[i - 1][0] # 동전과 금액의 수가 같을 때 하나의 경우의 수로 표현
    # 주어진 동전 금액과 개수를 입력받아서 dp 리스트에 저장한 것을 다음 회차에 적용하면서 체크한다.
    for price in range(1, T + 1):
        dp[i][price] = dp[i - 1][price]
        for cnt in range(1, n + 1):
            # 큰 골자는 1 ~ T까지의 금액을 돌면서 입력받은 동전과 그 개수를 곱하면서 해당하는 금액일 때
            # 이전까지 구했던 금액의 경우의 수와 더해서 업데이트한다.
            # 즉, 각 금액으로 입력받은 동전 금액과 개수를 곱하면서 경우의 수를 구하고,
            # 이전에 구했던 경우의 수 테이블에 따라 입력받은 것을 계속 더해준다.
            if price - p * cnt >= 0:
                dp[i][price] += dp[i - 1][price - p * cnt]
            else:
                break

print(dp[k][T])
