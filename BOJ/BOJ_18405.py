# Baekjoon Online Judge - 18405번. 경쟁적 전염


def bfs():
    new_list = []
    while virus_list:
        num, x, y = virus_list.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y]
                new_list.append((board[x][y], nx, ny))
    return new_list


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
virus_list = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            virus_list.append((board[i][j], i, j))
# 번호가 낮은 종류의 바이러스부터 증식하기 때문에 정렬을 해준다
virus_list.sort(key=lambda x: x[0])
for _ in range(S):
    virus_list = bfs()
    if len(virus_list) == 0:
        break
    # 마찬가지로 bfs를 통해 이동한 새로운 정보를 갖고 정렬을 해준다
    virus_list.sort(key=lambda x: x[0])
print(board[X - 1][Y - 1])
