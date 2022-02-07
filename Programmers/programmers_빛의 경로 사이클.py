# 하좌상우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def solution(grid):
    answer = []
    # 각 행, 열, 방향에 대한 방문체크 해야됨
    row_len = len(grid)
    col_len = len(grid[0])
    visited = [[[False] * 4 for _ in range(col_len)] for _ in range(row_len)]
    # 방문체크 => [4방향, 행, 열]
    for i in range(row_len):  # 행
        for j in range(col_len):  # 열
            for k in range(4):  # 4방향(하좌상우)
                # 방문하지 않았을 때만 실행(사이클 형성되지 않은 곳)
                if not visited[i][j][k]:
                    result = search(grid, visited, i, j, k, row_len, col_len)  # 사이클 찾기
                    if result != 0:
                        answer.append(result)
    answer.sort()  # 오름차순 정렬 !!!
    return answer


def search(grid, visited, nx, ny, nz, r, c):
    length = 0
    x, y, z = nx, ny, nz
    visited[nx][ny][nz] = True
    # dx, dy의 4방향이 하좌상우로 놨을 때 L이면 -1, R이면 +1을 통해 방향을 정한다
    while True:
        x = (x + dx[z]) % r
        y = (y + dy[z]) % c
        length += 1
        if grid[x][y] == 'L':  # 해당 공간이 L인 경우
            z = (z - 1) % 4
        elif grid[x][y] == 'R':  #
            z = (z + 1) % 4
        # 방문 했으면 사이클이 생성된 것 or 이미 방문한 곳
        if visited[x][y][z]:
            if (x, y, z) == (nx, ny, nz):  # 사이클이 형성됐다면
                return length
            else:
                return 0
        visited[x][y][z] = True

