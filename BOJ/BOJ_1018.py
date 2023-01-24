# Baekjoon Online Judge - 1018번. 체스판 다시 칠하기


def check(i, j, arr):
    temp = 0
    for x in range(8):
        for y in range(8):
            if board[i + x][j + y] != arr[x][y]:
                temp += 1
    return temp


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
start_B = []
start_W = []
W = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
B = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
for i in range(1, 9):
    if i % 2:
        start_B.append(B)
        start_W.append(W)
    else:
        start_B.append(W)
        start_W.append(B)

result = 987654321
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        cnt_W = check(i, j, start_W)
        cnt_B = check(i, j, start_B)
        result = min(result, min(cnt_W, cnt_B))
print(result)
