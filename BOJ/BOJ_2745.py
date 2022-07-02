# Baekjoon Online Judge - 2745번. 진법 변환

N, B = map(str, input().split())
B = int(B)
result = 0
alphabets = {}
for i in range(26):
    alphabets[chr(65 + i)] = 10 + i

idx = len(N) - 1
for alpha in N:
    if alpha.isalpha():
        result += alphabets[alpha] * (B ** idx)
    else:
        alpha = int(alpha)
        result += alpha * (B ** idx)
    idx -= 1
print(result)

