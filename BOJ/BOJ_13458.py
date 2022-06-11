# Baekjoon Online Judge - 13458번. 시험 감독

N = int(input())
examinees = list(map(int, input().split()))
B, C = map(int, input().split())
result = N
for A in examinees:
    A -= B
    if A > 0:
        if A % C:
            result += A // C + 1
        else:
            result += A // C
print(result)
