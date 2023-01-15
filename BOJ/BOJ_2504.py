# Baekjoon Online Judge - 2504번. 괄호의 값
# 값 계산하는 것을 찾아보았다. (, [이 있으면 해당 계산하는 수가 정해져있기 때문에 각각 맞는 2, 3값을 중간 계산 변수에 곱해준다
# 그러다가 )일 때 바로 앞에 것이 짝이 맞는 (이면 중간 계산 값을 더해주고 ()에 맞는 2로 나눈다.[]도 마찬가지
# 즉, 중간 계산값으로 계산을 하면서 되돌리는 과정 등을 진행한다.

string = input()
stack = []
result = 0
cnt = 1

for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
        cnt *= 2

    elif string[i] == '[':
        stack.append('[')
        cnt *= 3

    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break

        elif string[i - 1] == '(':
            result += cnt
        stack.pop()
        cnt //= 2
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break

        elif string[i - 1] == '[':
            result += cnt
        stack.pop()
        cnt //= 3

if stack:
    print(0)
else:
    print(result)
