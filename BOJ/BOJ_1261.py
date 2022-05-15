# Baekjoon Online Judge - 1261번. 알고스팟

from collections import deque


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    while q:
        x, y, cnt = q.popleft()
        if x == N - 1 and y == M - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if not visited[nx][ny]:
                # 벽이냐 아니냐에 따라 벽이 아닌 경우에는 우선순위를 둘 수 있으므로 맨 앞에다가 좌표 값을 놓는다.
                if maze[nx][ny]:
                    q.append((nx, ny, cnt + 1))
                else:
                    q.appendleft((nx, ny, cnt))
                visited[nx][ny] = True


M, N = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs())



