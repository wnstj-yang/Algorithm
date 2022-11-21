# SW Expert Academy - 5356번. 의석이의 세로로 말해요

T = int(input())

for tc in range(1, T + 1):
    result = ''
    max_len = 0
    words = []
    for _ in range(5):
        word = list(input())
        max_len = max(max_len, len(word))
        words.append(word)

    for i in range(5):
        length = len(words[i])
        words[i].extend([-1] * (max_len - length))

    for j in range(max_len):
        for i in range(5):
            if words[i][j] != -1:
                result += words[i][j]
    print('#{} {}'.format(tc, result))
