def solution(dartResult):
    answer = []
    state = ''
    for i in range(len(dartResult)):
        # 숫자라면 계속 더해주기
        if dartResult[i].isdecimal():
            state += dartResult[i]

        # S, D, T에따라 현재 숫자값에 제곱 혹은 세제곱 이후 리스트에 저장. state(수)는 초기화
        elif dartResult[i] == 'S':
            state = int(state)
            answer.append(state)
            state = ''

        elif dartResult[i] == 'D':
            state = int(state) ** 2
            answer.append(state)
            state = ''

        elif dartResult[i] == 'T':
            state = int(state) ** 3
            answer.append(state)
            state = ''

        else:
            # 값이 저장된 이후 옵션('*' or '#')에 따라 값 변동
            if dartResult[i] == '*':
                # 스타상을 받았으므로 현재값은 무조건 2를 곱하고
                answer[-1] *= 2
                # 이전 값이 존재하면 그 값도 2를 곱해준다
                if len(answer) > 1:
                    answer[-2] *= 2
            # 아차상이면 -1을 곱해줌
            else:
                answer[-1] *= -1

    return sum(answer)
