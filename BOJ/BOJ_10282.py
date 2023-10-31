# Baekjoon Online Judge - 10282번. 해킹

import heapq

INF = int(1e9)


def dijkstra(start):
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for com, d in computers[now]:
            cost = dist + d
            # 컴퓨터가 감염이 된다. 걸린 시간 갱신
            if cost < distance[com]:
                distance[com] = cost
                heapq.heappush(q, (cost, com))


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    computers = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        # a가 b에 의존이여서 b가 감염되면 a도 감염된다.
        computers[b].append((a, s))
    dijkstra(c)
    cnt, time = 0, 0
    for dist in distance:
        if dist != INF:
            cnt += 1
            time = max(time, dist)
    print(cnt, time)
