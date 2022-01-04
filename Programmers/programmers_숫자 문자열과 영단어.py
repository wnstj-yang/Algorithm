def solution(s):
    answer = ''
    numbers = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    temp = ''
    for alpha in s:
        # 주어진 문자열에서 숫자인지 판단 유무를 가림
        if alpha.isdecimal():
            answer += alpha  # 숫자인 경우 추가
        else:
            # temp라는 문자열 변수를 두어서 numbers안에 있는지 추가하면서 확인
            temp += alpha
            # 존재한다면 answer에 문자열을 추가하고 temp 초기화
            if temp in numbers:
                answer += numbers[temp]
                temp = ''

    return int(answer)