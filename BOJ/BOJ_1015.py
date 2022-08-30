# Baekjoon Online Judge - 1015번. 수열 정렬

N = int(input())
numbers = list(map(int, input().split()))
P = [-1] * N
# 가장 작은 값의 인덱스에 맞춰 0부터 넣어준다
for i in range(N):
    min_idx = numbers.index(min(numbers))
    numbers[min_idx] = 1001
    P[min_idx] = i
print(*P)
