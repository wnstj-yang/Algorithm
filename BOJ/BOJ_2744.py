# Baekjoon Online Judge - 2744번. 대소문자 바꾸기

words = input()

for word in words:
    ascii_num = ord(word)
    # 아스키코드가 대문자인 경우 소문자로
    if 65 <= ascii_num <= 90:
        print(chr(ascii_num + 32), end='')
    # 소문자를 대문자로 바꿔준다
    else:
        print(chr(ascii_num - 32), end='')
