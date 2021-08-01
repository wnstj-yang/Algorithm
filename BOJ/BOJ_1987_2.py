# Baekjoon Online Judge - 1987번. 알파벳
# visited를 포함하지 않은 경우 pypy3만 통과

# 상하좌우 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
    global ans

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        else:
            # 알파벳 26개중에 체크되지 않았다면
            if alpha_check[ord(board[nx][ny]) - 65] == 0:
                # 체크를 해주고 재귀
                alpha_check[ord(board[nx][ny]) - 65] = 1
                dfs(nx, ny, cnt+1)
                # 돌아왔을 때 다시 초기화 해주어 그 다음 경로가 갈 수 있게 만든다.
                alpha_check[ord(board[nx][ny]) - 65] = 0
    # 하나의 경로가 끝났을 때 최대 길이 체크
    if ans < cnt:
        ans = cnt


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
# 알파벳의 갯수 만큼 0으로 초기화하고 방문여부를 0과 1로 표시한다.
alpha_check = [0] * 26
ans = 0
alpha_check[ord(board[0][0]) - 65] = 1
dfs(0, 0, 1)
print(ans)
