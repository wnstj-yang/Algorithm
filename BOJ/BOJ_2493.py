# Baekjoon Online Judge - 2493번. 탑

N = int(input())
heights = list(map(int, input().split()))
stack = []
answer = []
for i in range(N):
    while stack:
        # 스택의 마지막 값이 현재 값보다 크다면 수신할 수 있기에 stack의 마지막 인덱스를 가져온다
        if stack[-1][1] > heights[i]:
            answer.append(stack[-1][0] + 1)
            break
        # 작다면 수신가능하지 않기 때문에 stack에 있는 마지막 값을 빼준다
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append((i, heights[i]))
print(*answer)
