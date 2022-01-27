# Baekjoon Online Judge -  15724번. 주지수
# sys 모듈사용한 입출력으로 시간을 좀 더 빠르게 함
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)] # 편의를 위해 한칸씩 늘림
K = int(input())
# 하나하나 더하는 방법을 택했을 때 N * M * K의 시간복잡도가 커질 수 있음
# 그래서 아래와 같이 누적합을 진행
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = (area[i-1][j-1] + dp[i][j-1] + dp[i-1][j]) - dp[i-1][j-1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print((dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2]) + dp[x1-1][y1-1])
