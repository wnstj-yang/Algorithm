def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)
    if len(stack) != 0:
        answer = False

    return answer
