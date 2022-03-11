def solution(s):
    answer = 0
    stack = []
    # stack을 통해 마지막에 들어간 값이 현재 넣을려는 것과 같다면 짝지어 제거한다.
    for alpha in s:
        if len(stack) != 0 and stack[-1] == alpha:
            stack.pop()
        # 그렇지 않은 경우 stack에 추가
        else:
            stack.append(alpha)
    # 다 비워졌으면 모두 짝지어서 잘 제거된 경우임
    if len(stack) == 0:
        answer = 1

    return answer
