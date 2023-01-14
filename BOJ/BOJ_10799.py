# Baekjoon Online Judge - 10799번. 쇠막대기

string = input()

stack = []
result = 0
for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
    else:
        if string[i - 1] == '(':
            stack.pop()
            result += len(stack)
        else:
            if stack:
                stack.pop()
                result += 1
print(result)
