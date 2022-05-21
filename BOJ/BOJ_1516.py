# Baekjoon Online Judge - 1516번. 게임 개발

from collections import deque


def topology_sort():
    result = [0] * (N + 1)
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 현재 노드 건물을 짓는데 소모되는 비용을 더해준다 
        # result[now]의 의미는 현재 노드까지 소모되는 선수 건물들의 비용 + 현재 노드의 건물 비용을 의미한다.
        result[now] += time[now]
        # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
        for i in graph[now]:
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            indegree[i] -= 1
            # i 노드의 건물을 짓기 전에 먼저 지어야되는 선수 건물의 비용의 비교를 통해 값 갱신
            # 예를 들어 4번 건물을 짓기 위해서 1, 3번 건물을 지어야함. 
            # 1번 건물 먼저 방문해서 result[4]는 0 -> 10
            # 3번 건물 방문 후 값이 14로 갱신되었고, result[4]는 기존의 10과 14를 비교해서 14로 갱신
            # 마지막으로 4번 건물 방문했을 때는 위의 (result[now] += time[now]) 과정에서 현재 건물 비용을 더해서
            # 14 + 4로 최종적으로 갱신되서 18이 됨
            result[i] = max(result[i], result[now])
            if indegree[i] == 0:
                q.append(i)
    for i in result[1:]:
        print(i)


N = int(input())
indegree = [0] * (N + 1)
time = [0] * (N + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(N + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    for j in info[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

topology_sort()
