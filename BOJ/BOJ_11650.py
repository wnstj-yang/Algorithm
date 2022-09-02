# Baekjoon Online Judge - 11650번. 좌표 정렬하기
# 입력에 대한 시간초과 대비를 위해서는 import sys활용


N = int(input())
coors = []
for _ in range(N):
    x, y = map(int, input().split())
    coors.append([x, y])
coors.sort(key=lambda x: (x[0], x[1]))
for x, y in coors:
    print(x, y)
