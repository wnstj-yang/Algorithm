# Baekjoon Online Judge - 1652번. 누울 자리를 찾아라

N = int(input())

board = [list(map(str, input())) for _ in range(N)]
row, col = 0, 0
# 가로 세로 모두 연속적으로 진행할 때 개수를 벽에 올 때까지 '.'이 몇 개 인지 판단하고, 2개 이상이면 누울 수 있다고 판단
# 그런 다음 다시 cnt을 0으로 초기화해서 다시 반복
for i in range(N):
    cnt = 0
    for j in range(N):
        if board[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                row += 1
            cnt = 0
    if cnt >= 2:
        row += 1

for j in range(N):
    cnt = 0
    for i in range(N):
        if board[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                col += 1
            cnt = 0
    if cnt >= 2:
        col += 1
print(row, col)
