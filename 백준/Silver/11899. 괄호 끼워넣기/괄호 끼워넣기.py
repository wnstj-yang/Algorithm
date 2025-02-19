string = input()
stack = []
for s in string:
    # 문자열이 '('이라면 스택에 추가
    if s == '(':
        stack.append(s)
    # 스택에 값이 있고, 현재 문자열이 ')', 스택에는 '('일 때 올바른 상태이므로 스택에서 제거
    elif stack and s == ')' and stack[-1] == '(':
        stack.pop()
    # 이외 값들을 스택에 추가
    else:
        stack.append(s)
print(len(stack))
