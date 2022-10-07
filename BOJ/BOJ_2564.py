# Baekjoon Online Judge - 2564번. 경비원

# (0, 0)을 기준으로 오른쪽으로 나아가면서 거리를 확인
def calc(num, y):
    if num == 1:
        return y

    elif num == 2:
        return N + M + N - y

    elif num == 3:
        return N + M + N + M - y

    else:
        return N + y


N, M = map(int, input().split())
K = int(input())
board = [[0] * N for _ in range(M)]
stores = []
result = 0
dg = 0
for _ in range(K):
    x, y = map(int, input().split())
    stores.append((x, y))

x, y = map(int, input().split())
dg = calc(x, y)
total_dist = 2 * (N + M)
for x, y in stores:
    dist = calc(x, y)
    side = abs(dist - dg)
    # 한쪽 거리를 알고 있으므로 전체 거리에서 뺀 나머지와 최소값을 비교
    reverse_side = total_dist - side
    result += min(side, reverse_side)
print(result)

