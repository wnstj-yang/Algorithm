# Baekjoon Online Judge - 2738번. 행렬 덧셈

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        result[i][j] = arr[i][j] + arr2[i][j]
for i in result:
    print(*i)
