# SW Expert Academy - 15230번. 알파벳 공부

T = int(input())

for tc in range(1, T + 1):
    word = input()
    now = 97
    result = 0
    # 연속해서 순서대로 이어지지 않는 알파벳이면 끝
    for i in range(len(word)):
        next1 = ord(word[i])
        if now == next1:
            now = next1 + 1
            result += 1
        else:
            break

    print('#{} {}'.format(tc, result))

