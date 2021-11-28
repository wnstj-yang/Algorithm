# Baekjoon Online Judge - 17086번. 아기 상어 2

from collections import deque

# 왼쪽 대각선부터 시계방향
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

# bfs 통한 최단 거리 구하기
def bfs():
    while sharks:
        x, y = sharks.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                # 상어를 이동하면서 거리 값을 넣는다.
                if area[nx][ny] == 0:
                    sharks.append((nx, ny))
                    area[nx][ny] = area[x][y] + 1


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
# 각 영역의 상어 위치들을 구한다.
sharks = deque()
for i in range(N):
    for j in range(M):
        if area[i][j] == 1:
            sharks.append((i, j))
bfs()
max_num = 0
for i in range(N):
    for j in range(M):
        if area[i][j] > max_num:
            max_num = area[i][j]
# 각 칸의 거리이므로 1을 빼준다
print(max_num - 1)
