# Baekjoon Online Judge - 14426번. 접두사 찾기

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
originals, targets = [], []
result = 0
for _ in range(N):
    originals.append(input().rstrip())
for _ in range(M):
    targets.append(input().rstrip())

for target in targets:
    for original in originals:
        is_prefix = True
        for i in range(len(target)):
            if target[i] != original[i]:
                is_prefix = False
                break
        if is_prefix:
            result += 1
            break
print(result)




