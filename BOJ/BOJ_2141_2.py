# Baekjoon Online Judge - 2141번. 우체국 second try

import sys
input = sys.stdin.readline

N = int(input())
people = 0
info = []
for _ in range(N):
    x, y = map(int, input().split())
    info.append((x, y))
    people += y
info.sort() # 마을 순서대로 표현

cnt = 0
for i in range(N):
    cnt += info[i][1]
    if cnt >= people / 2:
        print(info[i][0])
        break
