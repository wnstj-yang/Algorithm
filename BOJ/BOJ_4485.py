# Baekjoon Online Judge - 4485번. 녹색 옷 입은 애가 젤다지?

import heapq


def dijkstra(idx):
    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    INF = 987654321
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # arr안의 값들을 가중치로 생각하면서 각 좌표들을 돌고 목적지까지 최소 값을 구해나간다
    while q:
        dist, x, y = heapq.heappop(q)
        if x == N - 1 and y == N - 1:
            print('Problem {}: {}'.format(idx, dist))
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            cost = dist + arr[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))


idx = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(N)]
        dijkstra(idx)
        idx += 1
