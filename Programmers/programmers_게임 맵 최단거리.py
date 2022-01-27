from collections import deque


def solution(maps):
    answer = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    q = deque()
    q.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    # bfs를 통해 최단경로를 구한다
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            answer = visited[x][y]
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return answer