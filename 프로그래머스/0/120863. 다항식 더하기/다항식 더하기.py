def solution(polynomial):
    answer = ''
    with_x = 0
    number = 0
    polynomial = polynomial.split(' ')
    for item in polynomial:
        if len(item) >= 2:
            if item[-1] == 'x':
                with_x += int(item[:-1])
            elif item[0] != '+':
                number += int(item)
        else:
            if item[0] == 'x':
                with_x += 1
            elif item[0] != '+':
                number += int(item[0])
    if number == 0:
        if with_x <= 1:
            answer = 'x'
        else:
            answer = str(with_x) + 'x'
    elif with_x == 0:
        answer = str(number)
    else:
        if with_x <= 1:
            answer = 'x' + ' + ' + str(number)
        else:
            answer = str(with_x) + 'x' + ' + ' + str(number)
    return answer