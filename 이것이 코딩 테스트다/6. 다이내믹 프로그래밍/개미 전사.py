# 다이내믹 프로그래밍 - 220p. 개미 전사

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * 101 # 3 <= N <= 100
dp[0] = arr[0]
dp[1] = max(dp[0], arr[1])
# dp 리스트는 하나의 값이 현재 위치까지의 최대 값을 넣는 것이다.
# 그래서 비교를 i - 1번째까지 최대 값과 i - 2번째에서 i와 겹치지 않게 더할 수 있으므로
# arr[i] + dp[i - 2]의 값을 더해서 dp[i - 1]과 비교하는 것이다.
for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
print(dp[N - 1])


# 4
# 1 3 1 5