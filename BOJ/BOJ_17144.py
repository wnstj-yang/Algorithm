# Baekjoon Online Judge - 17144번. 미세먼지 안녕!

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 미세먼지 확산시키기
def spread():
    q = deque()
    for i in range(R):
        for j in range(C):
            if dust[i][j] > 0:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        cnt = 0
        if dust[x][y] >= 5:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= R or ny < 0 or ny >= C or dust[nx][ny] != -1:
                    continue
                # 5보다 크거나 같을 때만 적용 ( 시간 줄임 )
                dust[nx][ny] += dust[x][y] // 5
                cnt += 1
            dust[x][y] = dust[x][y] - ((dust[x][y] // 5) * cnt)


# 공기청정기 바람 불기
def send_wind():
    # 공기청정기 윗 부분
    # 1. 왼쪽 -> 오른쪽
    tmp_1 = dust[air_purifier[0][0]][1]
    dust[air_purifier[0][0]][1] = 0
    for i in range(2, C-1):
        tmp_2 = dust[air_purifier[0][0]][i]
        dust[air_purifier[0][0]][i] = tmp_1
        tmp_1 = tmp_2
    # 2. 위로 올라가는 부분
    for i in range(air_purifier[0][0], 0, -1):
        tmp_2 = dust[i][C-1]
        dust[i][C-1] = tmp_1
        tmp_1 = tmp_2
    # 3. 오른쪽 -> 왼쪽
    for i in range(C-1, 0, -1):
        tmp_2 = dust[0][i]
        dust[0][i] = tmp_1
        tmp_1 = tmp_2
    # 4. 아래로 내려가는 부분(공기청정기까지)
    for i in range(air_purifier[0][0]):
        tmp_2 = dust[i][0]
        dust[i][0] = tmp_1
        tmp_1 = tmp_2
    # 공기청정기 아랫 부분
    # 1. 왼쪽 -> 오른쪽
    tmp_1 = dust[air_purifier[1][0]][1]
    dust[air_purifier[1][0]][1] = 0
    for i in range(2, C-1):
        tmp_2 = dust[air_purifier[1][0]][i]
        dust[air_purifier[1][0]][i] = tmp_1
        tmp_1 = tmp_2
    # 2. 아래로 내려가는 부분
    for i in range(air_purifier[1][0], R-1):
        tmp_2 = dust[i][C-1]
        dust[i][C-1] = tmp_1
        tmp_1 = tmp_2
    # 3. 오른쪽 -> 왼쪽
    for i in range(C-1, 0, -1):
        tmp_2 = dust[R-1][i]
        dust[R-1][i] = tmp_1
        tmp_1 = tmp_2
    # 4. 위로 올라가는 부분(공기청정기까지)
    for i in range(R-1, air_purifier[1][0], -1):
        tmp_2 = dust[i][0]
        dust[i][0] = tmp_1
        tmp_1 = tmp_2


R, C, T = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(R)]
air_purifier = []
for i in range(R):
    for j in range(C):
        if dust[i][j] == -1:
            air_purifier.append((i, j))
while T > 0:
    spread()
    send_wind()
    T -= 1
ans = 0
for i in range(R):
    for j in range(C):
        if dust[i][j] != 0:
            ans += dust[i][j]
print(ans)
