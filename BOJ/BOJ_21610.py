# Baekjoon Online Judge - 21610번. 마법사 상어와 비바라기

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
cloud = []
cloud.append((N-1, 0))
cloud.append((N-1, 1))
cloud.append((N-2, 0))
cloud.append((N-2, 1))

for i in range(M):
    d, s = map(int, input().split())
    visited = [[False] * N for _ in range(N)]
    moved_cloud = []
    # 구름 이동시키기
    for j in range(len(cloud)):
        nx = cloud[j][0] + dx[d-1] * s
        ny = cloud[j][1] + dy[d-1] * s
        # 이동 시 행열연결이므로 범위를 벗어났는지 체크
        # 0보다 작으면 + N / N과 같거나 크면 - N
        if nx < 0:
            while True:
                nx += N
                if nx >= 0:
                    break
        elif nx >= N:
            while True:
                nx -= N
                if nx < N:
                    break
        if ny < 0:
            while True:
                ny += N
                if ny >= 0:
                    break
        elif ny >= N:
            while True:
                ny -= N
                if ny < N:
                    break
        moved_cloud.append((nx, ny))
        # 구름 있는 칸에 + 1
        area[nx][ny] += 1
        # 방문 표시로 다음 구름을 확인
        visited[nx][ny] = True
    for j in range(len(moved_cloud)):
        # 1, 3, 5, 7번째의 방향이 대각선임
        for k in range(1, 8, 2):
            nx = moved_cloud[j][0] + dx[k]
            ny = moved_cloud[j][1] + dy[k]
            # 이동과 달리 구름 대각선에서 물의 양 더할 때 범위 벗어나면 X
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 대각선에서 물 존재하면 + 1
            if area[nx][ny] > 0:
                area[moved_cloud[j][0]][moved_cloud[j][1]] += 1
    cloud = []
    # 새로이 구름 추가
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and area[x][y] >= 2:
                cloud.append((x, y))
                area[x][y] -= 2
ans = 0
for i in range(N):
    for j in range(N):
        ans += area[i][j]
print(ans)

