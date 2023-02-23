# 구현 - 유형별 문제. 치킨 배달 / 332p

from itertools import combinations


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chickens = []
homes = []
answer = 987654321
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chickens.append((i, j))
        elif board[i][j] == 1:
            homes.append((i, j))


for m in range(1, M + 1):
    for item in combinations(chickens, m):
        result = 0
        for h_x, h_y in homes:
            cnt = 987654321
            for c_x, c_y in item:
                temp = abs(h_x - c_x) + abs(h_y - c_y)
                cnt = min(temp, cnt)
            result += cnt
        answer = min(result, answer)
print(answer)
