# Baekjoon Online Judge - 1051번. 숫자 정사각형


N, M = map(int, input().split())
arr = []
result = 0
for _ in range(N):
    arr.append(list(map(int, input())))

min_val = min(N, M) # 정사각형을 만들기 위해 N과 M값중 최소를 구함

# 하나씩 다 돌며 정사각형을 만들 수 있는 꼭지점들을 체크해준다
for i in range(N):
    for j in range(M):
        for k in range(min_val):
            if i + k < N and j + k < M and (arr[i][j] == arr[i + k][j] == arr[i][j + k] == arr[i + k][j + k]):
                result = max(result, (k + 1) ** 2)
print(result)
