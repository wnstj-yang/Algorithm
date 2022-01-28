# Baekjoon Online Judge - 15900번. 나무 탈출
# 각각 게임말 하나씩을 리프노드에서 가진 것이 아니라
# 각 리프노드에 하나씩 게임말이 존재하는 것임... 하..
from collections import deque


def bfs():
    visited = [False] * (N + 1)
    q = deque()
    visited[1] = True
    q.append((1, 0))
    result = 0
    while q:
        n, cnt = q.popleft()
        # 현재 노드가 루트 노드가 아니고 리프 노드일 때 깊이를 더해준다
        if len(graph[n]) == 1 and n != 1:
            result += cnt
            continue
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                q.append((i, cnt+1))
    return result


# 리프노드 -> 루트노드 대신 루트노드 -> 리프노드의 깊이를 구한다
# 좀 더 효율적이다.
N = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = bfs()
if ans % 2:
    print('Yes')
else:
    print('No')



