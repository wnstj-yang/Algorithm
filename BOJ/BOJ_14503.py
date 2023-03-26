# Baekjoon Online Judge - 14503번. 로봇 청소기


def check_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return True
    else:
        return False


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 북동남서(상우하좌)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0
while True:
    # 1. 현재 칸이 청소되지 않은 경우 청소
    if board[r][c] == 0:
        board[r][c] = 2
        answer += 1
    isCleaned = True
    # 2. 주변 4칸을 살펴서 청소 유무를 본다
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if check_range(nr, nc):
            continue

        if board[nr][nc] == 0:
            isCleaned = False
            break
    # 3. 청소되지 않은 칸이 있다면 반시계
    if isCleaned:
        back_d = (d + 2) % 4
        nr = r + dr[back_d]
        nc = c + dc[back_d]
        if check_range(nr, nc):
            continue
        if board[nr][nc] == 1:
            break
        r, c = nr, nc
    else:
        d = (d - 1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if check_range(nr, nc):
            continue
        if board[nr][nc] == 0:
            r, c = nr, nc
print(answer)
