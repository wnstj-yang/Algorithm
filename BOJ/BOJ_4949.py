# Baekjoon Online Judge - 4949번. 균형잡힌 세상

while True:
    _string = input()
    if _string == '.':
        break
    stack = []
    check = True
    for char in _string:
        # '('와 '['인 경우 stack에 넣는다. ( 균형잡힐 수 있는 후보 )
        if char == '(' or char == '[':
            stack.append(char)
        # 오른쪽 소괄호인 경우
        elif char == ')':
            # stack이 비어있거나 stack안의 값이 대괄호인경우라면 X
            if len(stack) == 0 or stack[-1] == '[':
                check = False
                break
            else:
                stack.pop()
        # 오른쪽 대괄호인 경우
        elif char == ']':
            # stack이 비어있거나 stack안의 값이 소괄호인경우라면 X
            if len(stack) == 0 or stack[-1] == '(':
                check = False
                break
            else:
                stack.pop()
    if check:
        # 여기서 stack이 비어있지 않다면 균형잡히지 않을 수 있어서 체크해주어야 한다.
        # Ex) [()][. 의 문자열이 들어오면 마지막 '['이 stack에 남아있기 때문
        if len(stack) != 0:
            print('no')
        else:
            print('yes')
    else:
        print('no')
