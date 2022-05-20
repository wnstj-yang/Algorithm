# Baekjoon Online Judge - 13699번. 점화식


n = int(input())
dp = [0] * 36
dp[0], dp[1] = 1, 1
for i in range(2, n + 1):
    cnt, e = 0, i - 1 # 점화식에 따라 앞의 수 * 뒤에서부터 수
    for j in range(i):
        cnt += (dp[j] * dp[e])
        e -= 1
    dp[i] = cnt
print(dp[n])
