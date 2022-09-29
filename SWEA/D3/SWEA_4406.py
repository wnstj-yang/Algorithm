# SW Expert Academy - 4406번. 모음이 보이지 않는 사람


T = int(input())

for tc in range(1, T + 1):
    word = input()
    visited = [1] * len(word)
    result = ''
    for i in range(len(word)):
        if word[i] in ['a', 'e', 'i', 'o', 'u']:
            visited[i] = 0
    for i in range(len(word)):
        if visited[i]:
            result += word[i]
    print('#{} {}'.format(tc, result))

