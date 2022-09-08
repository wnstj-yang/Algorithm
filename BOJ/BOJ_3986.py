# Baekjoon Online Judge - 3986번. 좋은 단어


N = int(input())
result = 0
for _ in range(N):
    word = input()
    stack = []
    for alpha in word:
        if len(stack) == 0:
            stack.append(alpha)
        else:
            if alpha == stack[-1]:
                stack.pop()
            else:
                stack.append(alpha)
    if len(stack) == 0:
        result += 1
print(result)