# SW Expert Academy - 10912번. 외로운 문자

T = int(input())

for tc in range(1, T + 1):
    word = list(input())
    result = []
    for i in range(len(word)):
        if word[i] not in result:
            result.append(word[i])
        else:
            result.remove(word[i])
    result.sort()
    if len(result):
        print('#{} {}'.format(tc, ''.join(result)))
    else:
        print('#{} Good'.format(tc))

