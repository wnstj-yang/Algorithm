# Baekjoon Online Judge - 28278번. 스택 2

import sys

input = sys.stdin.readline


N = int(input())
stack = []
for _ in range(N):
    K = list(map(int, input().split()))
    if K[0] == 1:
        stack.append(K[1])
    elif K[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif K[0] == 3:
        print(len(stack))
    elif K[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)