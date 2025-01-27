class Solution(object):
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        time = 1
        x, y = 0, 0
        result = [matrix[x][y]]
        # 우하좌상
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0
        visited = [[False] * n for _ in range(m)]
        visited[x][y] = True
        while time < m * n:
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                d = (d + 1) % 4
                nx = x + dx[d]
                ny = y + dy[d]
            if not visited[nx][ny]:
                visited[nx][ny] = True
                result.append(matrix[nx][ny])
            x, y = nx, ny
            time += 1
        return result