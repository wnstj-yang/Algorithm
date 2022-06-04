# Baekjoon Online Judge - 1259번. 팰린드롬수

while True:
    num = input()
    if int(num) == 0:
        break
    else:
        if num == num[::-1]:
            print('yes')
        else:
            print('no')
