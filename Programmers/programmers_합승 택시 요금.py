import heapq


def dijkstra(start, n):
    global graph
    q = []
    INF = int(1e9)
    dist = [INF] * (n + 1)
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if cost > dist[now]:
            continue

        for i in graph[now]:
            node, c = i
            result = cost + c
            if result < dist[node]:
                dist[node] = result
                heapq.heappush(q, (result, node))
    return dist


def solution(n, s, a, b, fares):
    global graph
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        x, y, c = fare
        graph[x].append((y, c))
        graph[y].append((x, c))
    s_distance = dijkstra(s, n)  # 시작점에서의 거리 정보
    answer = s_distance[a] + s_distance[b]  # 시작점 거리 정보 바탕으로 a와 b 서로 각각 갔을 때 합을 더한다.
    for i in range(1, n + 1):
        if i != s:
            m_distance = dijkstra(i, n)  # 중간 지점에서의 거리 정보
            # 시작점부터 i까지의 거리 값 + i부터 a까지의 거리 값 + i부터 b까지의 거리 값
            # 위의 계산과 기존의 answer 최소인 값을 비교해서 최소 값 저장
            answer = min(answer, s_distance[i] + m_distance[a] + m_distance[b])

    return answer
