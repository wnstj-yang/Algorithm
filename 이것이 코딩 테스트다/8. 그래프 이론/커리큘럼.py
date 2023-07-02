# 그래프 이론 - 커리큘럼. 303p
# 위상정렬

from collections import deque


def topology_sort():
    q = deque()
    result = list(time)
    # 1. 진입 차수가 0인 노드들을 큐에 추가해준다
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        # 2. 큐에서 뺀 노드들을 돌면서 진입차수를 하나씩 줄인다.
        for i in graph[node]:
            indegree[i] -= 1
            # 최대 시간으로 잡아야 그 이전 선수과목(들) 중 최대값으로 해야 만족할 수 있기 때문임
            result[i] = max(result[i], result[node] + time[i])
            # 3. 연결된 노드의 진입 차수가 0인 경우에 해당 노드를 큐에 추가하여 방향을 거스르지 않게 만든다
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, N + 1):
        print(result[i])


N = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
time = [0] * (N + 1)
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    time[i] = info[0] # 각 강의시간을 저장하는 이유는 최소를 구해야 하기 때문
    for node in info[1:-1]:
        indegree[i] += 1
        graph[node].append(i)

topology_sort()

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 10
# 20
# 14
# 18
# 17