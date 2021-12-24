def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ':
            answer += ' '
            continue
        num = ord(char)  # 아스키코드
        # 대문자인 경우 65를 빼준 후 26으로 나머지연산
        if 65 <= num <= 90:
            num -= 65
            num = ((num + n) % 26) + 65
            answer += chr(num)
        # 대문자가 아니면 소문자이므로 97을 빼준 후 26으로 나머지연산
        else:
            num -= 97
            num = ((num + n) % 26) + 97
            answer += chr(num)

    return answer