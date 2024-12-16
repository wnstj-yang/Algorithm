N = int(input())
for _ in range(N):
    string = input()
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack and s == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(1)
            break
    if stack:
        print('NO')
    else:
        print('YES')