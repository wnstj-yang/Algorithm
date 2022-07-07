# Baekjoon Online Judge - 1236번. 성 지키기

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
row, col = 0, 0

for i in range(N):
    if 'X' not in arr[i]:
        row += 1

for j in range(M):
    check = True
    for i in range(N):
        if 'X' in arr[i][j]:
            check = False
            break
    if check:
        col += 1
print(max(row, col))
