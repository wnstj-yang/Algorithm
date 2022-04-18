# 118~119p 실전 문제 - 게임 개발

N, M = map(int, input().split())
x, y, direction = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# 북동남서 == 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited[x][y] = 1
result = 1
while True:
    check = True # 4방향 모두 이동가능한지 판단 기준
    # 4방향으로 방문하면서(시계 반대방향으로) 이동할 수 있는지 체크
    for _ in range(4):
        direction = (direction - 1) % 4
        nx = x + dx[direction]
        ny = y + dy[direction]
        if visited[nx][ny] == 0 and board[nx][ny] == 0:
            visited[nx][ny] = 1
            x, y = nx, ny
            result += 1
            check = False
            break
    # 4방향 모두 가지 못할 때 뒤로 한 칸 이동. 뒤에 바다라면 끝
    if check:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if board[nx][ny] == 1:
            break
        else:
            x, y = nx, ny
print(result)
# 예제 - 1
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
# 출력 - 1
# 3
