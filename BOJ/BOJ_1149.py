# Baekjoon Online Judge - 1149번. RGB 거리

N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):
    # 빨간 집 일 때 이전의 파란, 초록 집의 최소 값과 현재 빨간 집의 값을 더해 중복없이 합을 구한다.
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    # 위의 과정을 아래 초록, 파란집에 따라 동일하다.
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]
# 마지막 까지 구한 최소의 값을 구해서 출력
print(min(dp[N - 1]))
