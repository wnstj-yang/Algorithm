# Baekjoon Online Judge - 16948번. 데스 나이트


dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
board = [[-1] * N for _ in range(N)]
q = []
q.append((r1, c1))
board[r1][c1] = 0
while q:
    x, y = q.pop(0)
    if x == r2 and y == c2:
        break

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] == -1:
            q.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

print(board[r2][c2])
