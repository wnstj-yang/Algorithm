def solution(s, skip, index):
    answer = ''
    for alpha in s: # 주어진 문자열 순회
        # 반복하다 도는 알파벳인 alpha의 아스키코드값과 소문자로 구성되어있기 때문에
        # 0 ~ 25의 값으로 초기화하기 위해 97을 빼준다
        a_idx = ord(alpha) - 97
        # alpha의 위치에서부터 index의 길이까지의 문자열을 구한다
        # 26으로 나머지를 하는 이유는 z->a형태로 넘어가는 경우도 있기 때문에 처리해준다
        temp = ''.join([chr((a_idx + i) % 26 + 97) for i in range(1, index + 1)])
        while True:
            alphaIn = False # skip안에 알파벳이 존재하는지 확인
            for t in skip:
                if t in temp:
                    # 마지막 위치의 알파벳에서 그 다음 알파벳으로 추가해주기 위해 계산
                    num = (ord(temp[-1]) - 97 + 1) % 26
                    # 같은 문자가 존재할 수 있기때문에 앞의 문자를 공백으로 바꿔준다
                    temp = temp.replace(t, '', 1)
                    temp += chr(num + 97) # 공백으로 바꿔진 이후 새로운 문자를 뒤에 추가
                    alphaIn = True # skip안의 알파벳이 존재한다
            # skip안에 알파벳이 없는 경우라면 끝
            if not alphaIn:
                break
        answer += temp[-1] # 가장 마지막의 알파벳을 추가해준다
    return answer
