# Baekjoon Online Judge - 14499번. 주사위 굴리기


def move(order):
    global x, y
    dx, dy = direction[order]
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        return
    # 1. 주사위를 굴린다.
    if order == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4] # 동
    elif order == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]  # 서
    elif order == 3:
        dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]  # 북
    else:
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2] # 남
    # 2. 굴린 이후에 주사위의 윗 면에 있는 수를 출력
    print(dice[6])
    # 3. 이후 주사위의 바닥면과 이동한 지도의 칸과 비교하여 복사 및 0으로 초기화 등 진행
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[1]
    else:
        dice[1], maps[nx][ny] = maps[nx][ny], 0
    # 4. 좌표 초기화
    x, y = nx, ny


N, M, x, y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
# 1: 우, 2: 좌, 3: 상, 4: 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = {
    1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]
}
dice = [0] * 7
orders = list(map(int, input().split()))

for order in orders:
    move(order)
