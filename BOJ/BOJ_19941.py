# Baekjoon Online Judge - 19941번. 햄버거 분배

N, K = map(int, input().split())

info = list(map(str, input()))
result = 0
for i in range(N):
    if info[i] == 'P':
        for j in range(max(i - K, 0), min(i + K + 1, N)):
            if info[j] == 'H':
                info[j] = 0
                result += 1
                break
print(result)
