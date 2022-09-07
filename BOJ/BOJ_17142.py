# Baekjoon Online Judge - 17142번. 연구소 3


from collections import deque


def combi(idx, k):
    if k == M:
        comb_list.append(list(candi))
        return

    for i in range(idx, len(virus_coor)):
        if not visited[i]:
            visited[i] = True
            candi[k] = i
            combi(i, k + 1)
            visited[i] = False


def bfs(active):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    time = 0

    for i in active:
        x, y = virus_coor[i][0], virus_coor[i][1]
        q.append((x, y))
        visited[x][y] = 0 # 활성화

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visited[nx][ny] == -1:
                # 빈 공간이라면 시간을 늘려주고, 가장 큰 시간을 구한다.
                if arr[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    time = max(visited[nx][ny], time)
                # 기존의 바이러스였다면 비활성화이므로 활성화 시켜준다
                elif arr[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    v_wall = 0
    for line in visited:
        v_wall += line.count(-1)
    # 퍼진 이후에 -1의 개수 = 기존의 벽의 개수 성립하지 않으면 빈 공간에 바이러스가 모두 퍼지지 않았다는 의미이다.
    if v_wall != wall_cnt:
        return 987654321
    return time


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
virus_coor = []
comb_list = []
wall_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_coor.append((i, j))
        if arr[i][j] == 1:
            wall_cnt += 1
# 바이러스의 개수를 M의 개수만큼 조합으로 구한 후 아래 bfs를 돌린다.
candi = [0] * M
visited = [False] * len(virus_coor)
combi(0, 0)
result = 987654321
# bfs를 돌면서 최소 시간을 구하면 된다.
for active in comb_list:
    result = min(result, bfs(active))

if result == 987654321:
    print(-1)
else:
    print(result)

