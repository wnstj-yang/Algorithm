# Baekjoon Online Judge - 12605번. 단어순서 뒤집기

N = int(input())

for i in range(1, N + 1):
    case = list(input().split(' '))
    case.reverse()
    print('Case #{}: {}'.format(i, ' '.join(case)))
