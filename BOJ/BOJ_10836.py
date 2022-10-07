# Baekjoon Online Judge - 10836번. 여왕벌


def put(numbers):
    x, y = M - 1, 0
    idx = 0
    while x > 0:
        board[x][y] += numbers[idx]
        idx += 1
        x -= 1

    while y < M:
        board[x][y] += numbers[idx]
        idx += 1
        y += 1


M, N = map(int, input().split())

board = [[1] * M for _ in range(M)]
num_list = [0] * (2 * M - 1)
# 한 번에 다 더해주기. 어차피 한 칸위의 행에 있는 열의 값을 가져올거임.
for _ in range(N):
    x, y, z = map(int, input().split())
    for i in range(x, x + y):
        num_list[i] += 1
    for i in range(x + y, 2 * M - 1):
        num_list[i] += 2

put(num_list)
# 위쪽이 항상 왼쪽보다 크게 된다.
for i in range(1, M):
    for j in range(1, M):
        board[i][j] = board[i - 1][j]

for i in board:
    print(*i)


