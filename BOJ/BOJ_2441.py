# Baekjoon Online Judge - 2441번. 별 찍기 - 4

N = int(input())

for i in range(N, 0, -1):
    print(' ' * (N - i), end='')
    print('*' * i)
