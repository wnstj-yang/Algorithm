# DFS/BFS 유형별 문제. 346p - 괄호 변환

def balanced(w):
    stack = []
    for i in range(2, len(w)):
        temp = w[:i]
        left = temp.count('(')
        right = temp.count(')')
        if left == right:
            return (temp, w[i:])
    return (w, '')


def alright(w):
    stack = []
    for s in w:
        if len(stack) > 0 and stack[-1] == '(' and s == ')':
            stack.pop()
        else:
            stack.append(s)
    if len(stack) == 0:
        return True
    else:
        return False


def check(v):
    if v == '':
        return ''
    a, b = balanced(v)
    temp = ''
    if alright(a):
        a += check(b)
        return a
    else:
        temp += '('
        temp += check(b)
        temp += ')'
        reverse_temp = ''
        for r in a[1:-1]:
            if r == '(':
                reverse_temp += ')'
            else:
                reverse_temp += '('
        temp += reverse_temp
        return temp


def solution(p):
    answer = ''
    N = len(p)
    if alright(p):
        return p
    answer = check(p)

    return answer
