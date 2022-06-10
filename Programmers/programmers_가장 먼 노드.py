from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] * (n + 1) for _ in range(n + 1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    # 1부터 각 노드의 거리가 몇인지 체크함과 동시에 방문 표시 또한 진행한다.
    distance = [-1] * (n + 1)
    distance[1] = 0
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for i in graph[node]:
            # 거리가 -1이라면 방문하지 않은 곳을 의미하고, 현재 노드까지에서 거리 + 1을 해준다.
            if distance[i] == -1:
                distance[i] = distance[node] + 1
                q.append(i)
    long_len = max(distance)
    # 가장 먼 노드의 값을 구하고 개수가 몇개인지 카운트해서 답으로 처리
    answer = distance.count(long_len)
    return answer
