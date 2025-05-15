def solution(order):
    answer = 0
    for num in str(order):
        if num == '3' or num == '6' or num == '9':
            answer += 1
    return answer