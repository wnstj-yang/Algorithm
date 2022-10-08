# Baekjoon Online Judge - 11279번. 최대 힙

import heapq
import sys

input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num:
        heapq.heappush(q, -num)
    else:
        if len(q):
            print(-heapq.heappop(q))
        else:
            print(0)
