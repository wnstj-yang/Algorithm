# Baekjoon Online Judge - 16232번. 텔레포트 정거장
# pypy3 통과
from collections import deque


def bfs(x):
    q = deque()
    q.append((x, 0))
    visited[x] = True
    while q:
        n, cnt = q.popleft()
        # 현재 위치에서 -1, +1 값을 넣어준다.
        # 따로 처리하다보니 메모리초과...?
        pos[n].append(n-1)
        pos[n].append(n+1)
        for i in pos[n]:
            # 방문하지 않고 범위에서 벗어나지 않았을 때 queue추가
            if 1 <= i <= N and not visited[i]:
                q.append((i, cnt+1))
                visited[i] = True
                # 도착했다면 끝 (최소임)
                if i == E:
                    return cnt + 1


N, M = map(int, input().split())
S, E = map(int, input().split())
pos = [[] for _ in range(N+1)]
visited = [False] * (N+1)
# 텔레포트가 하나가 아닐 수도 있는 점 또한 고려사항
# 즉, 점 마다 하나인데 여러 개가 연결될 수 있음
for _ in range(M):
    x, y = map(int, input().split())
    pos[x].append(y)
    pos[y].append(x)
print(bfs(S))

