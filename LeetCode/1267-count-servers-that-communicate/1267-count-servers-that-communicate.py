from collections import deque

class Solution(object):
    def countServers(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        ans = 0
        # 같은 행, 열 => 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    visited[i][j] = True
                    q = deque()
                    q.append((i, j))
                    connect_list = [(i, j)]
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            tx, ty = x, y
                            while True:
                                nx = tx + dx[k]
                                ny = ty + dy[k]
                                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                    break
                                if not visited[nx][ny] and grid[nx][ny] == 1:
                                    visited[nx][ny] = True
                                    q.append((nx, ny))
                                    connect_list.append((nx, ny))
                                tx, ty = nx, ny
                    if len(connect_list) > 1:
                        ans += len(connect_list)
        return ans