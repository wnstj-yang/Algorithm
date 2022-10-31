# # Baekjoon Online Judge - 18427번. 함께 블록 쌓기

N, M, H = map(int, input().split())
dp = [[1] + [0] * H for _ in range(N + 1)]
i = 1

for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        dp[i][num] += 1
        # 목표했던 곳만 하지 않은 이유는 그 이전의 값들로 목표 값을 만들 수 있기 때문이다.
        # i학생의 블록을 사용할 시 목표인 H값보다 작은 경우의 수들을 더해준다
        for j in range(1, H + 1):
            if j + num <= H:
                dp[i][j + num] += dp[i - 1][j]
    # i학생의 블록을 사용하지 않을 때 이전블록의 내용들을 더해준다 
    for j in range(1, H + 1):
        dp[i][j] += dp[i - 1][j]
    i += 1

print(dp[N][H] % 10007)
