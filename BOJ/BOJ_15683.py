# Baekjoon Online Judge - 15683번. 감시
# 복사를 덜 하는 방향으로 잡아보자

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 각 번호별 방향. 어떻게 짜야할지
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 3], [1, 3], [1, 2], [0, 2]],
             [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]], [[0, 1, 2, 3]]]


def dfs(cnt, arr):
    global ans
    if cctv_cnt == cnt:
        temp = 0
        visited = [item[:] for item in workspace]
        for j in range(cnt):
            # 순서대로 사무실이 있는 곳의 좌표를 방향과 연결이 가능하다
            # 즉, arr이 check_offcies의 사무실에 맞게 방향이 맞춰져 있음
            x, y = check_offices[j][0], check_offices[j][1]
            for d in arr[j]:
                c = 1
                while True:
                    # 한 방향에서 범위 벗어나거나 벽을 만날 때까지 진행
                    nx = x + dx[d] * c
                    ny = y + dy[d] * c
                    if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == 6:
                        break
                    else:
                        # 벽이 아니라면 다른사무실이거나 빈 공간인 경우 바꿔준다
                        if visited[nx][ny] != 6:
                            visited[nx][ny] = '#'
                            c += 1
                        else:
                            break
        for item in visited:
            temp += item.count(0)

        if ans > temp:
            ans = temp
        return
    # 사무실의 좌표와 어떤 CCTV종류인지 확인
    x, y, camera = check_offices[cnt]
    for i in direction[camera]:
        arr.append(i)
        dfs(cnt+1, arr)
        arr.pop()


N, M = map(int, input().split())
workspace = [list(map(int, input().split())) for _ in range(N)]
check_offices = []
cctv_cnt = 0
ans = 987654321
for i in range(N):
    for j in range(M):
        if 1 <= workspace[i][j] <= 5:
            check_offices.append((i, j, workspace[i][j]))
            cctv_cnt += 1
dfs(0, [])
print(ans)
