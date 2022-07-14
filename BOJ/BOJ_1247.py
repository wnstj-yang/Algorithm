# Baekjoon Online Judge - 1247번. 부호

import sys

input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    result = 0
    for _ in range(N):
        result += int(input())
    if result > 0:
        print('+')
    elif result == 0:
        print(0)
    else:
        print('-')
