# Baekjoon Online Judge - 1374번. 강의실

import heapq


N = int(input())
times = []
for _ in range(N):
    num, x, y = map(int, input().split())
    times.append((x, y))
# 시작 시간, 끝나는 시간 순으로 오름차순 정렬 
times.sort(key=lambda x:(x[0], x[1]))
min_time = int(1e10)
result = 0
q = [] # 끝나는 시간 모음 
for start, end in times:
    # 강의가 끝나는 시간이 존재하고, 현재 시작 시간이 가장 빨리 끝나는 강의 시간보다 크거나 같다면 회의실을 늘릴 강의실늘 늘릴 필요가 없다.
    if q and start >= q[0]:
        heapq.heappop(q)
    else:
        result += 1 # 강의실 증가 
    heapq.heappush(q, end)
print(result)