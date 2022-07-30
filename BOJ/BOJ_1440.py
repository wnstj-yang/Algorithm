# Baekjoon Online Judge - 1440번. 타임머신

from itertools import permutations
# 시, 분, 초 에 있는 값들로 순열을 구한다
perms = list(permutations(map(int, input().split(':'))))
result = 0
for h, m, s in perms:
    if 1 <= h <= 12 and 0 <= m < 60 and 0 <= s < 60:
        result += 1
print(result)
