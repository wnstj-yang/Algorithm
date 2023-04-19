N, M = map(int, input().split())
relations = [[0] * (N + 1) for _ in range(N + 1)]
edges = [[0] * 2 for _ in range(M + 1)]
result = set()
# edges는 간선의 수 /
# 인접행렬로 구성을 한다음에 O(NM)으로 시간을 줄인다. O(N^3)
# 점 하나와 변 하나로 삼각관계를 확인한다.
for i in range(1, M + 1):
    x, y = map(int, input().split())
    relations[x][y] = 1
    relations[y][x] = 1
    edges[i][0] = x
    edges[i][1] = y

isDetected = False
for A in range(1, N + 1):
    for j in range(1, M + 1):
        B, C = edges[j][0], edges[j][1]
        if relations[A][B] + relations[A][C] == 2:
            temp = [A, B, C]
            temp.sort()
            result.add(tuple(temp))
            if len(result) >= 2:
                isDetected = True
                break
    if isDetected:
        break
if isDetected:
    print('YES')
else:
    print('NO')


