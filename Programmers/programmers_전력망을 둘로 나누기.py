from collections import deque


def bfs(start, end, graph, n):
    visited = [False] * (n + 1)
    visited[end] = True
    visited[start] = True
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                q.append(i)
    return cnt

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    # 전선을 하나씩 끊으면서 개수 비교 진행
    for start, end in wires:
        # 시작점과 연결된 노드 수: result
        # 총 노드 수 - 시작점과 연결된 노드 수 = n - result
        # 위의 두 개의 수 차이의 최소화를 구하는 것
        result = bfs(start, end, graph, n)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))
    return answer
