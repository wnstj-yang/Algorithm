def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        str_num = str(num)
        is_target = True
        for n in str_num:
            if not (n == '5' or n =='0'):
                is_target = False
                break
        if is_target:
            answer.append(num)
    if len(answer) == 0:
        answer = [-1]
    return answer