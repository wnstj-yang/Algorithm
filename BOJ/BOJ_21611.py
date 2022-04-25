# Baekjoon Online Judge - 21611번. 마법사 상어와 블리자드

from collections import deque


def fill_empty_marbles():
    empty_spaces = deque()
    for x, y in marbles:
        # 비어 있는 공간이라면 큐에 넣음
        if board[x][y] == 0:
            empty_spaces.append((x, y))
        # 비어있는 공간이 있고 다음의 수가 0보다 크다면 계속 옮기면서 빈 공간을 채워나간다
        elif board[x][y] > 0 and empty_spaces:
            px, py = empty_spaces.popleft()
            board[px][py], board[x][y] = board[x][y], 0
            empty_spaces.append((x, y))


# 달팽이 형태의 각 좌표값들이 어떻게 흘러가는지 큐에 넣어서 확인한다.(상어 칸 제외 끝까지)
def get_coors():
    q = deque()
    x, y = N // 2, N // 2
    length = 1
    direct = 0
    while True:
        for _ in range(2):
            for i in range(length):
                nx = x + dx[direct]
                ny = y + dy[direct]
                if nx == 0 and ny == 0:
                    q.append((nx, ny))
                    return q

                q.append((nx, ny))
                x, y = nx, ny
            direct = (direct + 1) % 4
        length += 1


def explosive():
    explode_coors = deque()
    num = -1
    cnt = 0
    check = False
    for x, y in marbles:

        if board[x][y] == num:
            cnt += 1
            explode_coors.append((x, y))
        else:
            # 4개의 구슬이 연속되는 경우 개수를 카운트하고 해당하는 곳들만 0으로 초기화
            if cnt >= 4:
                check = True
                exploded_marbles_cnt[num] += cnt
            while explode_coors:
                ex, ey = explode_coors.popleft()
                if cnt >= 4:
                    board[ex][ey] = 0

            num = board[x][y]
            cnt = 1
            explode_coors.append((x, y))
    return check


def group_marbles():
    numbers = []
    num = -1
    num_cnt = 0
    for x, y in marbles:
        # 처음에는 -1로 초기화 되어있음. 이후 연속되는지 판단을 진행한다.
        if num == -1:
            num = board[x][y]
            num_cnt = 1
        else:
            if board[x][y] == num:
                num_cnt += 1
            else:
                numbers.append(num_cnt)
                numbers.append(num)
                num = board[x][y]
                num_cnt = 1

    idx = 0
    # 인덱싱을 통해서 범위를 벗어나가지 않게 그룹을 구한것들을 바탕으로 값을 넣음
    for x, y in marbles:
        if idx >= len(numbers):
            break
        board[x][y] = numbers[idx]
        idx += 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 좌하우상( 중앙에서부터 달팽이형태로 )
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
# !!!! 상하좌우로 얼음파편을 날리니 이게 꼭 필요했다...
explode_dx = [-1, 1, 0, 0]
explode_dy = [0, 0, -1, 1]
# 폭발된 번호들의 개수
exploded_marbles_cnt = [0, 0, 0, 0]
marbles = get_coors()
for _ in range(M):
    d, s = map(int, input().split())
    x, y = N // 2, N // 2
    # 1. 얼음 파편 날리기
    for i in range(1, s + 1):
        nx = x + explode_dx[d - 1] * i
        ny = y + explode_dy[d - 1] * i
        board[nx][ny] = 0
    # 2. 날려진 빈 공간을 주어진 숫자들로 채워넣는다
    fill_empty_marbles()
    # 3. 연속되는 구슬들이 있다면 폭발하고 빈공간 채우는 것 반복(없을 때 까지)
    while explosive():
        fill_empty_marbles()
    # 4. 각 구슬의 그룹을 만들어서 값을 다시 넣는다
    group_marbles()

print(exploded_marbles_cnt[1] + 2 * exploded_marbles_cnt[2] + 3 * exploded_marbles_cnt[3])
