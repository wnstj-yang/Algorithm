# 149~150p 실전 문제

from collections import deque


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == N - 1 and y == M - 1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
bfs()
print(visited[N - 1][M - 1])

# 예제 - 1
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 출력 - 1
# 10
