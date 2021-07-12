# Baekjoon Online Judge - 16932번. 모양 만들기

# 시간 초과에 대한 문제를 해결하기 위해
# 1이 모여있는 무리들을 구하고 무리들 간의 번호를 정하면서
# 시간을 줄인다.
from collections import deque

# 상하좌우 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[0] * M for _ in range(N)]

# area리스트를 통해 무리의 정보를 정한다.
area = [[0] * M for _ in range(N)]
area_cnt = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            # queue에는 값이 1인 것들의 좌표
            queue = deque()
            queue.append((i, j))

            # real_queue를 통해 추후에 cnt로 한 무리에 값이 몇인지 카운트해서
            # arr리스트에 초기화 해준다.
            real_queue = deque()
            real_queue.append((i, j))
            cnt = 1
            visited[i][j] = 1
            while queue:
                x, y = queue.popleft()
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    else:
                        if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                            real_queue.append((nx, ny))
                            cnt += 1
                            queue.append((nx, ny))
                            visited[nx][ny] = 1

            # 한 무리에 1의 개수가 몇인지 arr에 초기화를 해줌과 동시에
            # area에도 해당 무리의 번호를 붙여서 무리들간의 구분
            while real_queue:
                a, b = real_queue.popleft()
                arr[a][b] = cnt
                area[a][b] = area_cnt
            area_cnt += 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result = 1
            check_area = []
            for z in range(4):
                nx = i + dx[z]
                ny = j + dy[z]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                else:
                    if arr[nx][ny] != 0 and area[nx][ny] not in check_area:
                        result += arr[nx][ny]
                        check_area.append(area[nx][ny])
            if result > ans:
                ans = result

print(ans)
