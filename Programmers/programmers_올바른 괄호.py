def solution(s):
    answer = True
    # l => '(' 개수, r => ')' 개수
    l, r = 0, 0
    # 중간에 개수체크
    check = False
    for item in s:
        if item == '(':
            l += 1
        else:
            r += 1
            # 중간에 '(' 개수보다 ')' 개수가 더 많으면 틀림
            if r > l:
                check = True
                break
    if check:
        answer = False
    # check조건에 걸리지 않더라도
    if answer:
        # l과 r의 개수가 같지 않다면 올바르지 않은 괄호를 뜻함
        if l != r:
            answer = False

    return answer