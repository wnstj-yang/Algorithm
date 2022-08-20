# Baekjoon Online Judge - 1388번. 바닥 장식


N, M = map(int, input().split())
result = 0
arr = [list(map(str, input())) for _ in range(N)]
# 가로, 세로로 나무판자가 같은 것들을 개수를 세준다음 전체에서 빼준다. 그러면 필요한 나무 판자 개수 구하기 가능
for i in range(N):
    for j in range(M - 1):
        if arr[i][j] == '-' and arr[i][j + 1] == '-':
            result += 1

for i in range(N - 1):
    for j in range(M):
        if arr[i][j] == '|' and arr[i + 1][j] == '|':
            result += 1
print(N * M - result)
