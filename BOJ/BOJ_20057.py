# Baekjoon Online Judge - 20057번. 마법사 상어와 토네이도


def spread(cur_x, cur_y, idx):
    global result
    sand_sum = 0
    # 도착했다면 끝
    if cur_y < 0:
        return

    for i, j, k in direction[idx]:
        nx, ny = cur_x + i, cur_y + j
        # a인 경우
        if k == 0:
            spread_sand = sand[cur_x][cur_y] - sand_sum
        else:
            spread_sand = int(sand[cur_x][cur_y] * k)
            sand_sum += spread_sand

        # 격자 밖으로 나간 모래의 양 더해줌
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            result += spread_sand
        # 범위를 벗어나지 않았다면 값 갱신
        else:
            sand[nx][ny] += spread_sand


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]
result = 0
x, y = N // 2, N // 2
# 좌하우상에 맞는 비율
left = [[-1, 1, 0.01], [1, 1, 0.01], [-2, 0, 0.02], [-1, 0, 0.07], [1, 0, 0.07], [2, 0, 0.02],
        [-1, -1, 0.1], [1, -1, 0.1], [0, -2, 0.05], [0, -1, 0]]
down = [[-1, -1, 0.01], [-1, 1, 0.01], [0, -2, 0.02], [0, -1, 0.07], [0, 1, 0.07], [0, 2, 0.02],
        [1, -1, 0.1], [1, 1, 0.1], [2, 0, 0.05], [1, 0, 0]]
right = [[-1, -1, 0.01], [1, -1, 0.01], [-2, 0, 0.02], [-1, 0, 0.07], [1, 0, 0.07], [2, 0, 0.02],
         [-1, 1, 0.1], [1, 1, 0.1], [0, 2, 0.05], [0, 1, 0]]
up = [[1, -1, 0.01], [1, 1, 0.01], [0, -2, 0.02], [0, -1, 0.07], [0, 1, 0.07], [0, 2, 0.02],
      [-1, -1, 0.1], [-1, 1, 0.1], [-2, 0, 0.05], [-1, 0, 0]]

# 좌하우상
direction ={0: left, 1: down, 2: right, 3: up}
# 이동시 좌표 값 - 좌하우상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cnt = 0
for i in range(2*N-1):
    # 나머지 연산을 통한 방향설정
    v = i % 4
    # 좌, 우에서 하나씩 늘어남
    if v == 0 or v == 2:
        cnt += 1
    # 주어진 방향에 따라 몇 칸 이동인지 cnt로 체크
    for _ in range(cnt):
        nx = x + dx[v]
        ny = y + dy[v]
        spread(nx, ny, v)
        # 좌표 위치 갱신
        x, y = nx, ny
print(result)


