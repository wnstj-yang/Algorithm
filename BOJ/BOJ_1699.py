# Baekjoon Online Judge - 1699번. 제곱수의 합
# pypy3 통과 - python3 시간 초과

N = int(input())
dp = [i for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, int(i ** 0.5) + 1):
        # 해당 수(i)의 루트까지의 범위로 제곱수 판단 
        # 예를 들어 12일 때 dp[12 - 1 ** 2] + 1 에서 1은 해당 1 ** 2의 개수를 추가한다는 의미 
        # dp[12 - 2 ** 2]에서 dp[8]에 + 1(2 ** 2)를 추가하면서 그 최소값을 찾는다
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)
print(dp[N])

