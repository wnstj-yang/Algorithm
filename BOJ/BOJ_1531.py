# Baekjoon Online Judge - 1531번. 투명


N, M = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] += 1

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > M:
            result += 1
print(result)
