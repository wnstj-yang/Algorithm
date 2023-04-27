# Baekjoon Online Judge - 1189번. 컴백홈

def dfs(x, y, cnt):
    global ans
    visited[x][y] = True # 깊이우선 탐색으로 해당 좌표에 방문 표시
    if cnt > K: # K보다 큰 경우 정답이 아니기 때문에 돌아간다
        return

    if x == 0 and y == C - 1: # 오른쪽 위인 집의 좌표인 경우
        if cnt == K: # K만큼의 거리가 소요됐다면 경우의 수 1 증가
            ans += 1
        return

    for i in range(4): # 상하좌우 4방향에 대해서 움직일 수 있는지 체크한다
        nx = x + dx[i]
        ny = y + dy[i]
        # 이동된 x, y 좌표인 nx, ny에 대해서 격자를 벗어나거나 T인 곳에 있다면 움직이지 못하므로 넘어간다
        if nx < 0 or nx >= R or ny < 0 or ny >= C or board[nx][ny] == 'T':
            continue
        # 방문하지 않고 움직일 수 있는 위치라면 깊이 탐색 진행
        if not visited[nx][ny] and board[nx][ny] == '.':
            dfs(nx, ny, cnt + 1) # 거리의 수를 1 증가하며 깊이 우선 탐색
            visited[nx][ny] = False # 깊이 우선 탐색을 다 진행한 이후 방문 표시해제


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C, K = map(int, input().split()) # R : 세로 길이 C : 가로 길이 K : 거리
board = [list(input()) for _ in range(R)] # 격자판
visited = [[False] * C for _ in range(R)] # 방문 표시
ans = 0 # 거리 K가 되는 경우의 수 개수
dfs(R - 1, 0, 1) # 왼쪽 아래 시작점부터 깊이 우선탐색 진행
print(ans)

