# Baekjoon Online Judge - 2563번. 색종이

N = int(input())
board = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(100 - 10 - x, 100 - x):
        for j in range(y, y + 10):
            board[i][j] = 1

result = 0
for i in range(101):
    for j in range(101):
        if board[i][j]:
            result += 1
print(result)
