# Baekjoon Online Judge - 11365번. !밀비 급일
# 뒤에서부터 출력
while True:
    encrypted = input()
    if encrypted == 'END':
        break
    else:
        for i in range(-1, -len(encrypted)-1, -1):
            print(encrypted[i], end='')
        print()
