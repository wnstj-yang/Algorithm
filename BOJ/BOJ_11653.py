# Baekjoon Online Judge - 11653번. 소인수분해

N = int(input())

for i in range(2, N + 1):
    # i로 나머지연산했을 때 나누어지면 분해지속
    while N % i == 0:
        print(i)
        N = N // i
