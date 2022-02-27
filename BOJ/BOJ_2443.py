# Baekjoon Online Judge - 2443번. 별 찍기 - 6

N = int(input())

for i in range(N, 0, -1):
    print(' ' * (N - i), end='')
    print('*' * (2 * i - 1))
