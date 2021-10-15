# Baekjoon Online Judge - 16973번. 직사각형 탈출
# 큐에 넣기 전에 일일이 다 검사하려면 시간초과가 발생
# 벽을 먼저 찾고 직사각형의 좌표로 범위벗어나는지 확인
# pypy 통과
from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    while q:
        x, y, cnt = q.popleft()
        if x == F_r - 1 and y == F_c - 1:
            return cnt
        for i in range(4):
            check = True
            nx = x + dx[i]
            ny = y + dy[i]
            # 시작점이 맵 밖을 나가면 X
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 직사각형의 시작점에서 대각선으로 끝점이 맵 밖에 나가면 X
            if nx + H - 1 >= N or ny + W - 1 >= M:
                continue
            # 범위 안에 벽이 있다면 X
            for r, c in walls:
                if nx <= r < nx + H and ny <= c < ny + W:
                    check = False
            # 방문하지 않은 곳이면서 위의 조건들을 통과했다면
            if check and visited[nx][ny] == 0:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1
    return -1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, S_r, S_c, F_r, F_c = map(int, input().split())
walls = []
# 벽이 있는 공간들을 찾는다
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            walls.append((i, j))
print(bfs(S_r-1, S_c-1))