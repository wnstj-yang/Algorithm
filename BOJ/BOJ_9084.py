# Baekjoon Online Judge - 9084번. 동전

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1) # 경우의 수들을 넣을 리스트
    dp[0] = 1 # 일종의 초기 값
    for coin in coins:
        for i in range(1, M + 1):
            if i - coin >= 0: # 현재 값에서 주어진 동전 값을 뺐을 때 범위를 벗어나지 않을 때
                dp[i] += dp[i - coin] # 각 동전까지의 경우의 수를 계속 더해나간다
    print(dp[M])
