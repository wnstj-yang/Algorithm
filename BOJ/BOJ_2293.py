# Baekjoon Online Judge - 2293번. 동전 1

n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1 # 주어진 숫자로만 만들 수 있는 것. 즉, 5 동전이 있으면 숫자 5를 5 동전 1개로 만들 수 있다는 의미
numbers = []
for _ in range(n):
    numbers.append(int(input()))
# 각 동전들을 사용해서 만들 수 있는 수의 개수 체크
for number in numbers:
    # 해당 동전으로 1 ~ k까지의 금액을 만들 수 있는 구성을 넣는다.
    for i in range(1, k + 1):
        # 현재 동전으로 금액을 만들 수 있는지 체크
        if i - number >= 0:
            # 이전까지 동전들로 사용해서 만드는 금액에서 현재 동전을 사용해서 금액을 만들 수 있을 때
            # 현재 금액에서의 만들 수 있는 총 개수 + 현재 금액에서 현재 동전 가치를 뺐을 때(=사용해서) 만들 수 있는 수
            # 즉, 예시에서 1, 2, 5의 동전 가치들을 잡았다면 1로 1 ~ 10(k)를 만들 수 있는 총 개수
            # 2로 1~ 10(k)를 만들 수 있는 총 개수, 5로 1 ~ 10(k)를 만들 수 있는 총 개수를 더하면서 구한다.
            dp[i] += dp[i - number]
print(dp[k])
