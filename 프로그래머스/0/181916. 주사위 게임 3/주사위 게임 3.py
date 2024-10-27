def solution(a, b, c, d):
    answer = 0
    result = {}
    for num in [a, b, c, d]:
        if num not in result:
            result[num] = 1
        else:
            result[num] += 1
    keys = list(result.keys())
    # 4개가 모두 같은 경우
    if len(keys) == 1:
        answer = 1111 * keys[0]
    elif len(keys) == 2:
        isTwo = False
        f_cnt= result[keys[0]]
        if f_cnt == 2:
            answer = (keys[0] + keys[1]) * abs(keys[0] - keys[1])
        else:
            if f_cnt == 3:
                answer = (10 * keys[0] + keys[1]) ** 2
            else:
                answer = (10 * keys[1] + keys[0]) ** 2
                
    elif len(keys) == 3:
        answer = 1
        for num in keys:
            if result[num] != 2:
                answer *= num
    else:
        answer += min(keys)
    return answer