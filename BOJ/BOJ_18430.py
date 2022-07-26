# Baekjoon Online Judge- 18430번. 무기 공학


def dfs(x, y, cnt):
    global result
    # 현재 좌표값에서 오른쪽으로 이동하는데 범위를 넘어서면 아래의 처음으로 이동
    if y == M:
        x += 1
        y = 0
    # 현재 세로 부분에서 범위가 넘어가면 끝이므로 최대값 설정
    if x == N:
        result = max(result, cnt)
        return

    # 현재 부메랑의 줌심 부분에서 방문하지 않았을때
    if not visited[x][y]:
        for i in range(4):
            x1, x2 = x + d[i][0], x + d[i][2]
            y1, y2 = y + d[i][1], y + d[i][3]
            # 부메랑들의 좌표에 범위를 넘어서지 않고 방문하지 않았을 때
            if 0 <= x1 < N and 0 <= x2 < N and 0 <= y1 < M and 0 <= y2 < M and not visited[x1][y1] and not visited[x2][y2]:
                visited[x][y] = True
                visited[x1][y1] = True
                visited[x2][y2] = True
                calcul = board[x][y] * 2 + board[x1][y1] + board[x2][y2]
                # 위의 결과값을 바탕으로 더해주고, 오른쪽으로 이동해준다 
                dfs(x, y + 1, cnt + calcul)
                visited[x][y] = False
                visited[x1][y1] = False
                visited[x2][y2] = False
    # 오른쪽으로 이동
    dfs(x, y + 1, cnt)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = 0
d = [[0, -1, 1, 0], [0, -1, -1, 0], [-1, 0, 0, 1], [0, 1, 1, 0]]
dfs(0, 0, 0)
print(result)
