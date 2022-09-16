# SW Expert Academy - 2050번. 알파벳을 숫자로 변환

string = input()
# 대문자만 입력으로 들어옴
for alpha in string:
    print(ord(alpha) - 64, end=' ')
