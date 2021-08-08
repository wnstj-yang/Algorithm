# Baekjoon Online Judge - 2589번. 보물섬

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    visited[x][y] = 0
    queue = deque()
    queue.append((x, y))
    temp = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                if visited[nx][ny] == -1 and treasure_map[nx][ny] == 'L':
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    # 가장 최근의 것이 긴 것
                    temp = visited[nx][ny]
    return temp


N, M = map(int, input().split())
treasure_map = [list(input()) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if treasure_map[i][j] == 'L':
            visited = [[-1] * M for _ in range(N)]
            max_dist = bfs(i, j)
            if ans < max_dist:
                ans = max_dist
print(ans)
