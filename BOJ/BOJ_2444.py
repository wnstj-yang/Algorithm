# Baekjoon Online Judge - 2444번. 별 찍기 - 7

N = int(input())

for i in range(1, N + 1):
    print(' ' * (N - i), end='')
    print('*' * (2 * i - 1))

for i in range(N - 1, 0, -1):
    print(' ' * (N - i), end='')
    print('*' * (2 * i - 1))
