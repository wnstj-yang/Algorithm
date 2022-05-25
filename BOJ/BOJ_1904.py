# Baekjoon Online Judge - 1904번. 01타일

N = int(input())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3, N + 1):
    # 중간중간 나머지연산을 하지 않을 경우 값이 매우 커지기 때문에 메모리초과가 발생
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
print(dp[N])
