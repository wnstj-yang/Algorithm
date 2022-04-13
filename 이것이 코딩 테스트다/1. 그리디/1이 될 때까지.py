# 99p 실전 문제 - 1이 될 때까지
N, K = map(int, input().split())
result = 0
while N != 1:
    if N % K == 0:
        result += 1
        N //= K
    else:
        result += 1
        N -= 1
print(result)