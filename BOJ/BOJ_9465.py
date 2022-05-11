# Baekjoon Online Judge - 9465번. 스티커
import sys
inpt = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    # 1일 경우 예외처리 2 이상이면 아래의 점화식 적용
    if N > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    # 해당 위치에 와있을 때 0번째 행에서는 1번째 i-1, i-2열의 아래쪽과의 최대 값을 비교해서 더한다
    # 마찬가지로 1번째 행에서는 0번째 i-1, i-2열의 위쪽과의 최대 값을 비교해서 더한다.
    # 즉, 현재 위치에서 각 행에서 올 수 있는 경우의 수를 체크해서 최대 값을 찾아 나선다
    for i in range(2, N):
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][-1], dp[1][-1]))
