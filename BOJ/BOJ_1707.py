# Baekjoon Online Judge - 1707번. 이분 그래프
from collections import deque
# 아래의 입력으로 받으면 Python3 통과 / 안쓰면 pypy3에서만 통과
# import sys
# input = sys.stdin.readline


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        adj = q.popleft()
        for cur_node in node[adj]:
            # 다음 정점 방문 시 자신과 인접한 정점은 자신과 다른 색으로 칠해야한다.
            if visited[cur_node] == 0:
                q.append(cur_node)
                visited[cur_node] = -visited[adj]
            # 두 가지의 색: 1, -1 로 이루어져 있으므로 합이 0이 아니라면 이분 그래프가 아님
            elif visited[cur_node] + visited[adj] != 0:
                return True
    return False


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    # 방문 표시이자 이분 그래프에 색칠을 칠한 정보
    visited = [0] * (V+1)
    result = False
    for _ in range(E):
        x, y = map(int, input().split())
        node[x].append(y)
        node[y].append(x)
    for i in range(1, V+1):
        if visited[i] == 0:
            result = bfs(i)
            # result로 받는 것이 True이면 이분 그래프가 아님을 의미
            if result:
                break
    if result:
        print('NO')
    else:
        print('YES')
