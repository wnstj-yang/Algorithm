# SW Expert Academy - 1949. [모의 SW 역량테스트] 등산로 조성


def dfs(x, y, cut, length):
    global answer
    # 길이 최대인지 지속 체크 
    answer = max(answer, length)
    visited[x][y] = True # 방문
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
            
        if not visited[nx][ny]:
            # 등산로 조성 시 현재보다 길이가 짧다면 진행
            if board[x][y] > board[nx][ny]:
                dfs(nx, ny, cut, length + 1)
            else:
                # 다음 위치 값이 현재 값보다 크고, 다음 위치 값 - 현재 위치 값 < 최대 깎을 수 있는 값
                # 위와 같이 성립하고 깎지 않은 경우에는 "최대 길이의 등산로를 조성"해야하므로 
                # 다음 위치 값에 현재 위치 값 - 1으로 깎은 후 진행한다
                if cut == 0 and board[nx][ny] - board[x][y] < K:
                    original = board[nx][ny] # 등산로 조성한 이후에 값을 다시 바꿔줘야 하므로 변수에 저장
                    board[nx][ny] = board[x][y] - 1
                    dfs(nx, ny, 1, length + 1)
                    board[nx][ny] = original
    visited[x][y] = False


T = int(input())
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_list = []
    max_val = 0
    answer = 0
    for i in range(N):
        max_val = max(max_val, max(board[i]))
    for i in range(N):
        for j in range(N):
            if board[i][j] == max_val:
                max_list.append((i, j))
    for x, y in max_list:
        dfs(x, y, False, 0)
    print('#{} {}'.format(tc, answer + 1))
