# SW Expert Academy - 1949번. [모의 SW 역량테스트] 등산로 조성

def check_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True


def dfs(isCutted, x, y, val, cnt):
    global result
    result = max(result, cnt)
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check_range(nx, ny) and not visited[nx][ny]:
            if board[nx][ny] >= val:
                # 최대 K깊이만큼 깎을 수 있는지 확인
                if not isCutted and board[nx][ny] - board[x][y] < K:
                    # 현재 값을 나타내는 val에서 현재 노드(x,y)에서 1을 빼주어야한다.
                    dfs(True, nx, ny, board[x][y] - 1, cnt + 1)

                continue
            else:
                dfs(isCutted, nx, ny, board[nx][ny], cnt + 1)

        else:
            continue
    # 4방향을 다돌고나서 확인하기 때문에 마지막에 방문처리 
    visited[x][y] = False

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, T + 1):
    result = 0
    N, K = map(int, input().split())
    board = []
    visited = [[False] * N for _ in range(N)]
    max_num = 0
    for _ in range(N):
        num_list = list(map(int, input().split()))
        max_num = max(max_num, max(num_list))
        board.append(num_list)
    max_coors = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == max_num:
                dfs(False, i, j, board[i][j], 1)

    print('#{} {}'.format(tc, result))
