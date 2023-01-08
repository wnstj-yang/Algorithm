# Baekjoon Online Judge - 11728번. 배열 합치기

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = A + B
result.sort()
print(*result)
