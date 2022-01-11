def solution(s):
    answer = []
    s = s.lower() # 주어진 문자열을 모두 소문자로 바꾼다
    # split()했을 때 공백이 여러개여도 하나로 인식 
    # split(' ') 공백이 여러개라도 하나씩 인식
    words = s.split(' ')
    for word in words:
        # 각각 공백일경우 추가해준다
        if word == '':
            answer.append('')
        else:
            # 공백이 아닐 때
            temp = list(word)
            # 아스키코드 사용하여 단어의 첫 문자가 소문자인 경우(숫자판단까지 진행)
            if not 65 <= ord(temp[0]) <= 90 and not temp[0].isdecimal():
                temp[0] = chr(ord(temp[0]) - 32) # 소문자의 경우 -32를 해주면 대문자로 변환이 된다(아스키코드)
            answer.append(''.join(temp))
    return ' '.join(answer)