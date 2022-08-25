# Baekjoon Online Judge - 2028번. 자기복제수

T = int(input())

for _ in range(T):
    N = input()
    result = str(int(N) ** 2)
    length = len(N)
    if result[-length:] == N:
        print('YES')
    else:
        print('NO')
