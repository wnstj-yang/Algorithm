# Baekjoon Online Judge - 18809번. Gaaaaaaaaaarden
# 조합을 잘 구현하는 것이 중점이였다.

from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 배양액 ( 조합 )
def avail(idx, green, red):
    global result
    # 배양액을 다 썼다면
    if green == 0 and red == 0:
        # 깊은 복사하면 시간이 오래걸려 리스트 슬라이싱으로 더 빠르게 복사함
        arr = [garden[:] for garden in ground]
        queue = deque()
        # 거리 표현을 한다. 초록, 빨간 배양액이 같은 시간에 만나 꽃이 되는지 확인하기 위함
        tmp_dist = [[-1] * M for _ in range(N)]
        # 초록색 배양액 먼저 뿌려주고
        for a in range(len(g_list)):
            x, y = g_list[a][0], g_list[a][1]
            arr[x][y] = 3  # 초록색 배양액
            tmp_dist[x][y] = 0  # 거리는 0으로 표시
            queue.append((x, y))

        # 그 다음 빨간색 배양액을 뿌려준다
        for b in range(len(r_list)):
            x, y = r_list[b][0], r_list[b][1]
            arr[x][y] = 4
            tmp_dist[x][y] = 0
            queue.append((x, y))
        # 이후에 배양액이 뿌려진 상태에서 퍼지게 한다
        cnt = spread(arr, queue, tmp_dist)
        if result < cnt:
            result = cnt
        return

    for k in range(idx, len(avail_space)):
        # 초록색 먼저하고 빨간색 다음에 하게끔 조합 2번 곱함
        if green > 0:
            g_list.append(avail_space[k])
            avail(k+1, green-1, red)
            g_list.pop()

        if red > 0:
            r_list.append(avail_space[k])
            avail(k+1, green, red-1)
            r_list.pop()


# 뿌린 배양액을 퍼지게 하다
def spread(arr, q, dist):
    cnt = 0
    # 초록색을 먼저 퍼트리고 빨간색을 퍼트려서 꽃을 만들 수 있는지 체크한다.
    while q:
        q_length = len(q)
        for _ in range(q_length):
            x, y = q.popleft()
            # 꽃만들어진 곳이면 넘어간다
            if arr[x][y] == 5:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                else:
                    # 0이면 호수이니 넘어간다
                    if arr[nx][ny] == 0:
                        continue
                    # 배양액이 퍼질 수 있는 곳이므로 체크한다
                    if arr[nx][ny] <= 2:
                        dist[nx][ny] = dist[x][y] + 1
                        arr[nx][ny] = arr[x][y]
                        q.append((nx, ny))
                    # 다음 볼 곳이 초록색이고 현재가 빨간색인 경우와 시간이 맞다면 꽃으로 확인
                    elif arr[nx][ny] == 3:
                        if arr[x][y] == 4 and dist[x][y] + 1 == dist[nx][ny]:
                            arr[nx][ny] = 5
                            cnt += 1
                    # 다음 볼 곳이 빨간색이고 현재가 초록색인 경우와 시간이 맞다면 꽃으로 확인
                    elif arr[nx][ny] == 4:
                        if arr[x][y] == 3 and dist[x][y] + 1 == dist[nx][ny]:
                            arr[nx][ny] = 5
                            cnt += 1
    return cnt


N, M, G, R = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
result = 0
avail_space = deque()
# 배양액 뿌릴 수 있는 좌표 구하기
for i in range(N):
    for j in range(M):
        if ground[i][j] == 2:
            avail_space.append((i, j))

# 빨간색, 초록색 배양액 담을 리스트 각각 만들어 놓음
r_list, g_list = [], []
avail(0, G, R)
print(result)
