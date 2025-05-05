def solution(my_string):
    calculations = my_string.split(' ')
    a, op, b = int(calculations[0]), calculations[1], int(calculations[2])
    answer = a + b if op == '+' else a - b
    for i in range(3, len(calculations) - 1, 2):
        if calculations[i] == '+':
            answer += int(calculations[i + 1])
        else:
            answer -= int(calculations[i + 1])
    return answer
        
        