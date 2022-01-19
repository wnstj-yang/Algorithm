# Baekjoon Online Judge - 17626번. Four Squares
# pypy3만 통과

N = int(input())
cnt = 0
dp = [0] * (N+1)
dp[0], dp[1] = 0, 1
# 제곱근을 구하고 제곱 수를 뺐을 때 5개로 만들어지는 경우가 있다.
# 반대도 마찬가지로 생각되어 하나의 규칙이 존재
# 값에 대한 최소 개수를 저장한다 / N보다 작거나 같은 제곱수를 찾은 후 가진 값에 + 1
# 예를 들어 9라고 할 때, 1부터 최소개수를 찾다가 3일 때 제곱하면 딱 1개가 나오므로
# 그 이전의 값들과 min함수로 비교한다
for i in range(2, N + 1):
    min_idx = 1e9
    j = 1
    while j ** 2 <= i:
        min_idx = min(min_idx, dp[i - j ** 2])
        j += 1
    dp[i] = min_idx + 1
print(dp[N])

