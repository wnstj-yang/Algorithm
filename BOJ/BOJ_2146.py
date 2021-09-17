# Baekjoon Online Judge - 2146번. 다리 만들기

from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, cnt):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    bridges[x][y] = cnt
    # 섬을 탐색하고 주어진 cnt값으로 섬을 구별한다
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            else:
                if visited[nx][ny] == 0 and bridges[nx][ny] == 1:
                    bridges[nx][ny] = cnt
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


def bfs2(num):
    queue = deque()
    # 거리 변수
    dist = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if bridges[i][j] == num:
                # 해당 섬에서 시작점은 0으로 초기화해준다 (거리를 구하기 때문)
                dist[i][j] = 0
                queue.append((i, j))
    # 최단거리 측정
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            else:
                # 다음 좌표에서 다른 섬을 만났을 때
                if bridges[nx][ny] > 0 and bridges[nx][ny] != num:
                    return dist[x][y]
                # 다음 좌표의 값과 현재 값을 비교할 필요 없이 이미 현재 위치에서 다시 덧붙여지는 것이기 때문에
                # 거리를 최소값으로 초기화된다.
                if bridges[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))


N = int(input())
bridges = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 2
for i in range(N):
    for j in range(N):
        if bridges[i][j] == 1:
            bfs(i, j, cnt)
            cnt += 1
# 최소 값 비교
ans = 987654321
for i in range(2, cnt):
    tmp = bfs2(i)
    # 최소값 비교
    if ans > tmp:
        ans = tmp
print(ans)
