num = 1
while True:
    string = input()
    stack = []
    result = 0
    if string[0] == '-':
        break
    for s in string:
        if s == '{':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            # }일 때 stack이 비어있으면 바꾼 상태로 넣어준다
            else:
                stack.append('{')
                result += 1
    result += len(stack) // 2 # { 개수의 절반이 뒤바꾸는 것이다.
    print('{}. {}'.format(num, result))
    num += 1