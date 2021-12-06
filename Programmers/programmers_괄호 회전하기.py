def solution(s):
    answer = 0
    check = ['(', '{', '[']
    s = list(s)
    idx = 0
    length = len(s)
    while idx < length:
        stack = []
        # 길이만큼 진행
        for i in range(len(s)):
            # 정답 여부의 flag
            check_ans = True
            # (, {, [ 인 경우 stack에 추가
            if s[i] in check:
                stack.append(s[i])
            else:
                # }}}와 같은 경우 혹은 괄호들의 짝이 안맞을 때 X
                if len(stack) == 0:
                    check_ans = False
                    break
                value = stack.pop()
                # 아래의 3 조건은 올바르지 않았을 때의 경우
                if value == '[' and s[i] != ']':
                    check_ans = False
                    break
                if value == '{' and s[i] != '}':
                    check_ans = False
                    break
                if value == '(' and s[i] != ')':
                    check_ans = False
                    break
        # 정답이고
        if check_ans:
            # stack이 비어있다면 => 올바른 괄호를 뜻함
            if len(stack) == 0:
                answer += 1
        # 한칸씩 왼쪽으로
        s.append(s.pop(0))
        idx += 1
    return answer