# 최단 경로 - 유형별. 플로이드 385p

N = int(input())
M = int(input())
INF = int(1e9)
dp = [[INF] * (N + 1) for _ in range(N + 1)] # 인접행렬

# a 에서 b로 가는 경로가 1개가 아닐 수 있기 때문에 최소인 값을 저장
for _ in range(M):
    a, b, c = map(int, input().split())
    if dp[a][b] > c:
        dp[a][b] = c

# 각 노드의 제자리는 0으로 초기화
for i in range(1, N + 1):
    dp[i][i] = 0

# 플로이드 와샬 알고리즘
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

# a 에서 b로 갈 수 없는 곳이라면 플로이드와샬 알고리즘 진행 이후에 0으로 초기화
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dp[i][j] == INF:
            dp[i][j] = 0

for item in dp[1:]:
    print(*item[1:])
