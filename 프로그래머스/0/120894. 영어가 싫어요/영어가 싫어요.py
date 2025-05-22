def solution(numbers):
    answer = ''
    index = 0
    target = {
        'zer': '0', 'one': '1', 'two': '2', 'thr': '3',
        'fou': '4', 'fiv': '5', 'six': '6', 'sev': '7',
        'eig': '8', 'nin': '9'
    }
    while index < len(numbers):
        num = numbers[index:index + 3]
        index += 3
        if num == 'thr' or num == 'sev' or num == 'eig':
            index += 2
        elif num == 'zer' or num == 'fou' or num == 'fiv' or num == 'nin':
            index += 1
        answer += target[num]
            
    return int(answer)