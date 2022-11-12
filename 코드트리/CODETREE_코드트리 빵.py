from collections import deque


# 편의점 찾기
def bfs(idx, x, y):
    q = deque()
    q.append((0, x, y))
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    candis = []
    while q:
        cnt, x, y = q.popleft()
        if board[x][y] == 1:
            candis.append((cnt, x, y))
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[nx][ny] and board[nx][ny] <= 2:
                q.append((cnt + 1, nx, ny))
                visited[nx][ny] = True
    candis.sort(key=lambda x: (x[0], x[1], x[2]))
    x, y = candis[0][1], candis[0][2] # 가장 가까운 곳
    board[x][y] = 2
    peoples[idx][0], peoples[idx][1] = x, y


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0
peoples = [[-1, -1] for _ in range(M)]
stores = []
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    stores.append([x, y])


while True:
    time += 1
    # 1. 편의점을 향해 1칸 움직이기
    for i in range(M):
        if peoples[i] == [-1, -1] or peoples[i] == stores[i]:
            continue
        # 현재 위치에서 4방향으로 범위를 벗어나지 않는 좌표들을 기준으로 편의점 위치까지 최단 거리를 구하고,
        # 최단 거리를 가진 4방향 중 1개 방향의 좌표값을 현재 위치로 지정(움직임)
        x, y = peoples[i]
        min_dist = 987654321
        min_x, min_y = x, y
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            q = deque()
            q.append((0, nx, ny))
            move_visited = [[False] * N for _ in range(N)]
            move_visited[nx][ny] = True
            while q:
                cnt, jx, jy = q.popleft()
                if jx == stores[i][0] and jy == stores[i][1]:
                    if min_dist > cnt:
                        min_dist = cnt
                        min_x, min_y = nx, ny
                        break
                for k in range(4):
                    tx = jx + dx[k]
                    ty = jy + dy[k]
                    if tx < 0 or tx >= N or ty < 0 or ty >= N:
                        continue
                    if not move_visited[tx][ty] and board[tx][ty] < 2:
                        q.append((cnt + 1, tx, ty))
                        move_visited[tx][ty] = True
        peoples[i] = [min_x, min_y]

    # 2. 편의점 도착 시 멈추고, 지나갈 수 없도록 표시
    for i in range(M):
        if peoples[i] == stores[i]:
            x, y = peoples[i]
            board[x][y] = 2
    # 모두 편의점까지 다 도착했는지 확인
    check = True
    for i in range(M):
        if peoples[i] != stores[i]:
            check = False
            break
    if check:
        print(time)
        break
    # 3. 격자 밖에 있는 사람들 번호 순으로 체크
    if time > M:
        continue
    bfs(time - 1, stores[time - 1][0], stores[time - 1][1])


