# 올바른지 판단
def check(p):
    # stack 사용 / ()이면 True, )( 이면 초반부터 틀려서 False
    stack = []
    for item in p:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True


def make_string(p):
    # 조건 1. 빈 문자열 반환
    if p == '':
        return ''
    # u, v를 구하기 위한 범위 index
    l, r = 0, 0
    u, v = '', ''
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        elif p[i] == ')':
            r += 1
        # u는 더이상 분리가 되지 않는다.
        if l == r:
            u, v = p[:i + 1], p[i + 1:]
            break
    # 조건 3. 올바른 괄호 문자열인지 확인
    if check(u):
        # 3-1에서 u에 이어 붙이고 v 재귀
        return u + make_string(v)

    # 올바른 문자열이 아닐 경우
    else:
        # 조건 4-1
        ans = '('
        # 조건 4-2
        ans += make_string(v)
        # 조건 4-3
        ans += ')'
        # 문자열이라 인덱스 슬라이싱으로 4-4조건
        for i in u[1:-1]:
            if i == '(':
                ans += ')'
            else:
                ans += '('
        # 조건 4-5
        return ans


def solution(p):
    answer = ''

    answer = make_string(p)

    return answer

