import sys

input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    order = list(map(int, input().split()))
    if len(order) > 1:
        num = order[1]
        stack.append(num)
    else:
        num = order[0]
        if num == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif num == 3:
            print(len(stack))
        elif num == 4:
            if stack:
                print(0)
            else:
                print(1)
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)