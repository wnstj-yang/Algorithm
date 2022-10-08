# Baekjoon Online Judge - 1927번. 최소 힙

import heapq, sys

input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num:
        heapq.heappush(q, num)
    else:
        if len(q):
            print(heapq.heappop(q))
        else:
            print(0)
