# Baekjoon Online Judge - 2156번. 포도주 시식

N = int(input())
numbers = [0]
for _ in range(N):
    numbers.append(int(input()))
dp = [0] * 10001
dp[1] = numbers[1]
if N > 1:
    dp[2] = numbers[1] + numbers[2]
# 최대의 가능성 3가지
# 1. 현재 위치에서 i - 1(이전)위치까지 최대 양의 합. 즉, 현재까지 마시게 되면 연속 3번 X의 조건에 부합하므로 이전까지의 합이 최대
# 2. 현재 위치 + 직전 위치(i - 1) + (i - 3)까지의 최대 양의 합이 최대인 경우.
# 3. 현재 위치 + (i - 2)위치 까지 최대양의 합이 최대인 경우.
for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 3] + numbers[i - 1] + numbers[i], dp[i - 2] + numbers[i])
print(dp[N])
