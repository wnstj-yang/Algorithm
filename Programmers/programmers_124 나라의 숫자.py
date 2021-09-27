def solution(n):
    answer = ''
    # n이 0이 될 때 까지 진행
    while n > 0:
        # 나머지 연산
        value = n % 3
        # 나머지 연산했을 때 0이면
        if value == 0:
            # 4를 먼저 채워주고 뒤에 문자열 추가
            answer = '4' + answer
            # 규칙에 따라 3으로 나눠준 몫에 -1을 하고 진행한다
            n = n // 3 - 1
        # 나머지 연산했을 때 1, 2이면
        else:
            # 그대로 문자열 1, 2로 만들어서 추가해준다
            answer = str(value) + answer
            # 몫은 그대로
            n = n // 3

    return answer