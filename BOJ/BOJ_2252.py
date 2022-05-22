# Baekjoon Online Judge - 2252번. 줄 세우기

from collections import deque


def topoplogy_sort():
    q = deque()
    result = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 진입 차수 내용에 따라 위상정렬된 결과에 현재 노드를 더해나간다.
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    # 줄 세운 결과
    print(*result)


N, M = map(int, input().split())
students = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # a가 b보다 먼저 앞에 와야한다.
    # a -> b로의 간선이 존재해서 b번의 진입차수는 1 증가
    indegree[b] += 1
topoplogy_sort()
