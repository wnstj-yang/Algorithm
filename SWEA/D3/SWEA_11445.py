# SW Expert Academy - 11445번. 무한 사전


T = int(input())

for tc in range(1, T + 1):
    word1 = input().rstrip()
    word2 = input().rstrip()
    word1 += 'a'

    if word1 != word2:
        print('#{} Y'.format(tc))
    else:
        print('#{} N'.format(tc))
