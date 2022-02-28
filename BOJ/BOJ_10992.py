# Baekjoon Online Judge - 10992번. 별 찍기 - 17

N = int(input())

for i in range(1, N + 1):
    if i == N:
        print('*' * (2 * N - 1))
    else:
        print(' ' * (N - i), end='')
        print('*', end='')
        print(' ' * (2 * (i - 1) - 1), end='')
        if i == 1:
            print()
            continue
        print('*')
