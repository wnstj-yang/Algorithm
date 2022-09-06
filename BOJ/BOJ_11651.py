# Baekjoon Online Judge - 11651번. 좌표 정렬하기 2


N = int(input())
coors = []
for _ in range(N):
    x, y = map(int, input().split())
    coors.append((x, y))
coors.sort(key=lambda x: (x[1], x[0]))
for x, y in coors:
    print(x, y)
