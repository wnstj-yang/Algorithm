# Baekjoon Online Judge - 3187번. 양치기 꿍

from collections import deque

# 상하좌우 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global sheep, wolf
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    temp_sheep, temp_wolf = 0, 0
    # 해당 좌표가 늑대거나 양이면 해당 임시로 개수 세는 변수에 카운트
    if farm[x][y] == 'v':
        temp_wolf += 1
    else:
        temp_sheep += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            else:
                # 탐색 시 좌표가 울타리가 아니면서 방문하지 않은 곳이라면
                if visited[nx][ny] == 0 and farm[nx][ny] != '#':
                    # 늑대인지 양인지 각 카운트
                    if farm[nx][ny] == 'v':
                        temp_wolf += 1
                    elif farm[nx][ny] == 'k':
                        temp_sheep += 1
                    # 울타리가 아니면 탐색한다.
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
    if temp_sheep > temp_wolf:
        sheep += temp_sheep
    else:
        wolf += temp_wolf


R, C = map(int, input().split())
farm = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
sheep, wolf = 0, 0
for i in range(R):
    for j in range(C):
        # 방문하지 않았고, 양이거나 늑대이면 탐색 시작
        if (farm[i][j] == 'v' or farm[i][j] == 'k') and visited[i][j] == 0:
            bfs(i, j)

print(sheep, wolf)
