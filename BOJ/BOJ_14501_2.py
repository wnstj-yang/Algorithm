# Baekjoon Online Judge - 14501번. 퇴사
# dp방식으로 핵심은 뒤에서부터 최대값을 체크해주는 것이다.

N = int(input())
answer = 0
numbers = []
dp = [0] * (N + 1)
for _ in range(N):
    a, b = map(int, input().split())
    numbers.append((a, b))

for i in range(N - 1, -1, -1):
    # 범위를 벗어난다면 이전까지의 최대 합
    if i + numbers[i][0] > N:
        dp[i] = dp[i + 1]
    # 범위 내에서 N + 1번째 날 기준 합과 N번째 날 금액 + Ti만큼 지난 후 금액의 합 중 최대 합
    else:
        dp[i] = max(dp[i + 1], numbers[i][1] + dp[i + numbers[i][0]])
print(dp[0])
