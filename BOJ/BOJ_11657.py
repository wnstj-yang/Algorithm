# Baekjoon Online Judge - 11657번. 타임머신

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정


def bellman_ford(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # 전체 n번의 라운드를 반복
    for i in range(n):
        # 매 반복마다 모든 간선을 확인
        for j in range(m):
            cur = edges[j][0] # 시작도시
            next_node = edges[j][1] # 도착도시
            cost = edges[j][2] # 걸리는 시간
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                # n번째 라운드에서도 값이 갱신되면 음수 순환이 존재(n-1번  반복 끝난 이후)
                if i == n - 1:
                    return True
    return False


# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a, b, c))

# 벨만 포드 알고리즘 수행
negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n + 1):
        # 도달할 수 없는 경우 -1 출력
        if distance[i] == INF:
            print(-1)
        # 도달할 수 있는 경우 거리 출력
        else:
            print(distance[i])
