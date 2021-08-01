# Baekjoon Online Judge - 1987번. 알파벳
# visited를 포함한 경우 pypy3만 통과

# 상하좌우 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
    global ans
    # 재귀를 돌면서 방문표시와 해당 알파벳을 방문했다는 표시
    visited[x][y] = 1
    alpha_check[ord(board[x][y]) - 65] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        else:
            # 방문하지 않았고, 알파벳이 겹치지 않는다면 방문 가능 !
            if alpha_check[ord(board[nx][ny]) - 65] == 0 and visited[nx][ny] == 0:
                dfs(nx, ny, cnt+1)
    # 다시 되돌아와서 방문 및 알파벳 초기화
    visited[x][y] = 0
    alpha_check[ord(board[x][y]) - 65] = 0
    if ans < cnt:
        ans = cnt


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
alpha_check = [0] * 26
ans = 0
dfs(0, 0, 1)
print(ans)
