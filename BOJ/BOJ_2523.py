# Baekjoon Online Judge - 2523번. 별 찍기 - 13

N = int(input())

for i in range(1, N + 1):
    print('*' * i)

for i in range(N - 1, 0, -1):
    print('*' * i)
