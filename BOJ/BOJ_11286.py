# Baekjoon Online Judge - 11286번. 절댓값 힙

import heapq
import sys

input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num:
        heapq.heappush(q, (abs(num), num))
    else:
        if len(q):
            info = heapq.heappop(q)
            print(info[1])
        else:
            print(0)
