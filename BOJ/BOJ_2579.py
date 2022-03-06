# Baekjoon Online Judge - 2579번. 계단 오르기

N = int(input())
stairs = [0] * 300
dp = [0] * 300
for i in range(N):
    stairs[i] = int(input())
# 3연속 되지 않고 최대의 합을 구한다.
dp[0] = stairs[0] # 첫 번째
dp[1] = stairs[0] + stairs[1] # 두 번째(1~2칸 합)
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2]) # 세 번째(2칸 + 1칸, 1칸 + 2칸)

for i in range(3, N):
    # 전전칸에서 올라왔을 때의 최대 합과 직전 칸에서 올라왔을 때의 최대 합 비교
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])
print(dp[N-1])
