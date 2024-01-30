# Baekjoon Online Judge - 1417 국회의원 선거

import heapq

q = []
N = int(input())
ans = int(input())
cnt = 0
for _ in range(N - 1):
    heapq.heappush(q, -int(input())) # 최대 힙
if N == 1:
    print(0)
else:
    while True:
        # 현재 다솜이가 가진 값이 우선순위 큐에 있는 가장 큰 값보다 크다면 끝
        if -q[0] < ans:
            break
        ans += 1 # 다솜이 표 증가
        num = heapq.heappop(q) + 1 # 최대힙이기 때문에 양수가 음수로 되어있으므로 1을 더해줘서 표를 빼준다
        heapq.heappush(q, num)
        cnt += 1
    print(cnt)
