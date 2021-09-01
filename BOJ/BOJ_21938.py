# Baekjoon Online Judge - 21938번. 영상처리
# 픽셀에 rgb가 포함되는 것을 파악해야함

from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                if visited[nx][ny] == 0 and pixels[nx][ny] == 255:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


N, M = map(int, input().split())
# rgb를 포함한 pixel의 리스트
pixels_rgb = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
# 계산완료된 픽셀의 값들
pixels = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        # 각 픽셀의 rgb값을 다 더하고 3으로 나눈 후
        pixels[i][j] = sum(pixels_rgb[i][3*j:3*(j+1)]) // 3
        # 이 것이 경계값 기준으로 0인지 255인지 판단
        if pixels[i][j] >= T:
            pixels[i][j] = 255
        else:
            pixels[i][j] = 0

visited = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and pixels[i][j] == 255:
            bfs(i, j)
            ans += 1
print(ans)

