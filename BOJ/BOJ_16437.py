# Baekjoon Online Judge - 16437번. 양 구출 작전

import sys
sys.setrecursionlimit(1234567) # 최대 깊이
input = sys.stdin.readline


def dfs(node):
    result = 0
    # 리프 노드에 왔을 때 양이라면 그 수를 반환
    if len(graph[node]) == 0:
        if info[node][0] == 'S':
            return info[node][1]
        else:
            return 0
    # 1번 노드부터 시작했으므로 연결되는 자식 노드들의 경로들을 거친 이후의 모든 합을 판단
    for i in graph[node]:
        result += dfs(i)

    # 경로를 올라오면서 현재 노드가 늑대 혹은 양인 경우에 따라 다른 판단
    if info[node][0] == 'W' and node != 1:
        result -= info[node][1]
        # 늑대가 더 많은 경우 result값이 0보다 작으므로 이를 0으로 처리
        if result < 0:
            result = 0
    elif info[node][0] == 'S':
        result += info[node][1]

    return result


N = int(input())
graph = [[] for _ in range(N + 1)]
info = {1: [0, 0]}
for i in range(2, N + 1):
    t, a, p = map(str, input().split())
    info[i] = [t, int(a)]
    graph[int(p)].append(i)

print(dfs(1))
