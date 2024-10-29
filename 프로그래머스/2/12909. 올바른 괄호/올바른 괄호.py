def solution(s):
    answer = True
    stack = []
    for l in s:
        if stack and stack[-1] == '(' and l == ')':
            stack.pop()
        else:
            stack.append(l)
    if stack:
        answer = False
    return answer