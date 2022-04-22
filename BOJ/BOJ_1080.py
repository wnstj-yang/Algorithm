# Baekjoon Online Judge - 1080번. 행렬

# 0 -> 1, 1 -> 0 과정 
def reverse_matrix(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0


N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
result = 0
# 3x3 행렬을 하나의 격자로 파악해서 진행하기 때문에 미리 범위를 지정함
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            reverse_matrix(i, j)
            result += 1

check = False
# 과정들을 거친 이후에 같은지 다른지 판단
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            result = -1
            check = True
            break
    if check:
        break
print(result)
