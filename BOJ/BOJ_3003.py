# Baekjoon Online Judge - 3003번. 킹, 퀸, 룩, 비숏, 나이트, 폰

whites = list(map(int, input().split()))
result = []
need = [1, 1, 2, 2, 2, 8]
for i in range(6):
    result.append(need[i] - whites[i])
print(*result)