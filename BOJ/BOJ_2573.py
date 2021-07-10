# Baekjoon Online Judge - 2573번. 빙산
# python3 시간초과 - pypy3 통과

from collections import deque


# 빙산 덩어리안의 값들을 줄인다.
def decrease_iceberg(queue):
    # 빙산 값에서 4방향으로 물이 있는지 확인해서 좌표값과 같이 넣는다.
    decrease_queue = deque()
    while queue:
        x, y = queue.popleft()
        temp = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                if iceberg[nx][ny] == 0:
                    # 임시로 물의 개수를 카운트
                    temp += 1
        # 좌표 값과 물의 개수를 카운트 한다.
        decrease_queue.append((x, y, temp))

    # 따로 decrease_queue 하는 이유는 위에서 물 개수 카운트하고 빼면 원래 빙산 상황이 반영이 안되기 때문
    while decrease_queue:
        x, y, water = decrease_queue.popleft()
        iceberg[x][y] -= water
        if iceberg[x][y] < 0:
            iceberg[x][y] = 0


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    temp_queue = deque()
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0 and visited[i][j] == 0:
                # cnt를 시간으로 본다
                cnt += 1
                # cnt가 1 초과면 빙산 덩어리가 2개 이상이라는 의미로 분리됨을 뜻하니까 끝낸다.
                if cnt > 1:
                    break

                # temp_queue로 빙산 덩어리 내 값들의 좌표를 구한다.
                temp_queue.append((i, j))
                # queue로 빙산 덩어리 내 값들의 좌표로 4방향 탐색해서 물이 있는지 확인하여 빙산 상황을 업데이트한다.
                queue.append((i, j))
                visited[i][j] = 1
                while temp_queue:
                    x, y = temp_queue.popleft()
                    for z in range(4):
                        nx = x + dx[z]
                        ny = y + dy[z]
                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue
                        else:
                            if iceberg[nx][ny] != 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                temp_queue.append((nx, ny))
                                queue.append((nx, ny))
        if cnt > 1:
            break

    # 빙산 덩어리가 없는 경우 끝 / 빙산이 다 녹을 때 까지 분리되지 않으면 0
    if cnt == 0:
        ans = 0
        break
    if cnt > 1:
        break
    else:
        decrease_iceberg(queue)
        # 시간 증가
        ans += 1
print(ans)

