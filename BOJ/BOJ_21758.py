# Baekjoon Online Judge - 21758번. 꿀 따기

# 벌통의 위치 => 맨 왼쪽, 맨 오른쪽, 가운데.

N = int(input())
numbers = list(map(int, input().split()))
result = 0
dp = [numbers[0]] # 시간초과 방지를 위해 누적잡 개념을 추가한다. 좌우로 합을 알아야하기 때문에 리스트에 추가하는 형태로 간다
for i in range(1, N):
    dp.append(dp[i - 1] + numbers[i])

# 1. 벌통 위치가 맨 왼쪽, 벌 하나는 맨 오른쪽에 위치
for i in range(N - 2, -1, -1):
    result = max(result, dp[N - 2] + dp[i] - numbers[i] * 2)

# 2. 벌통 위치가 맨 오른쪽, 벌 하나는 맨 왼쪽에 위치
for i in range(1, N - 1):
    result = max(result, dp[N - 1] - numbers[0] + dp[N - 1] - dp[i] - numbers[i])

# 3. 벌이 각각 맨 왼쪽과 오른쪽에 있고 벌통 위치가 그 가운데 중 하나
for i in range(1, N - 1):
    result = max(result, dp[N - 2] - numbers[0] + numbers[i])

print(result)
