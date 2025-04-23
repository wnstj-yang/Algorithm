def solution(quiz):
    answer = []
    for expression in quiz:
        num = expression.split(' ')
        result = num[-1]
        num1, num2 = num[0], num[2]
        operator = num[1]
        # 5개 이상이면 하나는 음수인 것이다.
        if len(num) > 5:
            # 1. 둘 다 음수인 경우
            if num[0] == '-' and num[3] == '-':
                num1, num2 = -num[1], -num[4]
                operator = num[2]
            # 2. 앞에만 음수인 경우
            elif num[0] == '-':
                num1, num2 = -num[1], num[3]
                operator = num[2]
            # 3. 뒤에만 음수인 경우
            elif num[2] == '-':
                num1, num2 = num[0], -num[3]
        calculate = 0
        if operator == '+':
            calculate = int(num1) + int(num2)
        else:
            calculate = int(num1) - int(num2)
        if calculate == int(result):
            answer.append('O')
        else:
            answer.append('X')
                    
    return answer