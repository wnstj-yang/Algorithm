import heapq


def dijkstra(N, info):
    INF = int(10e9)
    distance = [INF] * (N + 1)
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)  # dist는 현재 노드까지의 최소 거리
        # 현재 노드까지의 거리가 최단 거리로 저장된 곳보다 크다면 넘어간다(어차피 더해도 최단거리가 만들어지지 않음)
        if dist > distance[now]:
            continue
        # 현재 노드와 연결된 인접한 노드들 확인
        for i in info[now]:
            # i[0], i[1] = 인접 노드와의 거리, 인접 노드
            cost = dist + i[0]
            # 최단 거리로 저장된 것 보다 작다면 최단 거리 갱신
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

    return distance


def solution(N, road, K):
    answer = 0
    info = [[] for _ in range(N + 1)]
    # 양방향
    for edge in road:
        a, b, c = edge
        info[a].append((c, b))
        info[b].append((c, a))

    result = dijkstra(N, info)  # 1번 마을부터 각 마을간의 최단거리 구함
    # K이하인 마을들을 구함
    for i in range(1, len(result)):
        if result[i] <= K:
            answer += 1
    return answer
