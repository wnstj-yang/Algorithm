# Baekjoon Online Judge - 14426번. 접두사 찾기

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
originals = []
result = 0
for _ in range(N):
    originals.append(input().rstrip())
for _ in range(M):
    target = input().rstrip()
    for original in originals:
        if original[:len(target)] == target:
            result += 1
            break

print(result)
