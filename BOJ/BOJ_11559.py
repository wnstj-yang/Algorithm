# Baekjoon Online Judge - 11559번. Puyo Puyo


from collections import deque


def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    same_colors = []
    same_colors.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue

            if not visited[nx][ny] and field[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx, ny))
                same_colors.append((nx, ny))
    return same_colors


def gravity():
    for j in range(6):
        # 아래부터 올라오면서 아래로 떨어트린다
        for i in range(10, -1, -1):
            for k in range(11, i, -1):
                if field[i][j] != '.' and field[k][j] == '.':
                    field[k][j] = field[i][j]
                    field[i][j] = '.'
                    break


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
field = [list(map(str, input())) for _ in range(12)]
result = 0
# 1. 같은 색 4개 이상(상하좌우) 뿌요들을 한꺼번에 없앤다.
# 2. 이후 터진 애들을 모아서 중력영향으로 아래로 내린다.

while True:
    visited = [[False] * 6 for _ in range(12)]
    not_boomed = True
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and field[i][j] != '.':
                color_list = bfs(i, j, field[i][j])
                # 같은 색 뿌요들이 4개 이상일 경우 터지고 해당 좌표를 '.'로 초기화
                if len(color_list) >= 4:
                    not_boomed = False
                    for x, y in color_list:
                        field[x][y] = '.'
    # 터지지 않을 때 까지 진행
    if not_boomed:
        print(result)
        break
    else:
        result += 1
        # 중력 영향으로 아래로 떨어뜨린다.
        gravity()


