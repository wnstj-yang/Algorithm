# Baekjoon Online Judge - 10990번. 별 찍기 - 15

N = int(input())

for i in range(1, N + 1):
    print(' ' * (N - i), end='')
    print('*', end='')
    print(' ' * (2 * (i - 1) - 1), end='')
    if i == 1:
        print()
        continue
    print('*')
