# Baekjoon Online Judge - 11723번. 집합

import sys
input = sys.stdin.readline


M = int(input())
S = set()
for _ in range(M):
    info = input().split()
    if len(info) == 1:
        if info[0] == 'all':
            S = set(range(1, 21))
        else:
            S = set()
    else:
        if info[0] == 'add':
            S.add(int(info[1]))
        elif info[0] == 'remove':
            S.discard(int(info[1]))
        elif info[0] == 'check':
            if int(info[1]) in S:
                print(1)
            else:
                print(0)
        elif info[0] == 'toggle':
            num = int(info[1])
            if num in S:
                S.discard(num)
            else:
                S.add(num)
