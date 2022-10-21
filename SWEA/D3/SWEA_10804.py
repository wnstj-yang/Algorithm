# SW Expert Academy - 10804번. 문자열의 거울상

T = int(input())
change_alphas = {
    'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'
}
for tc in range(1, T + 1):
    word = input()
    word = word[::-1]
    result = ''
    for alpha in word:
        result += change_alphas[alpha]
    print('#{} {}'.format(tc, result))
