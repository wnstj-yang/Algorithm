# Baekjoon Online Judge - 15903번. 카드 합체 놀이
import heapq

q = []

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
for num in numbers:
    heapq.heappush(q, num)

for _ in range(M):
    x = heapq.heappop(q)
    y = heapq.heappop(q)
    heapq.heappush(q, x + y)
    heapq.heappush(q, x + y)

print(sum(q))
