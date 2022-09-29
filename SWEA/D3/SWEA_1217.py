# SW Expert Academy - 1217번. [S/W 문제해결 기본] 4일차 - 거듭 제곱


def mul(val, M):
    if M == 0:
        return 1
    return val * mul(val, M - 1)


for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, mul(N, M)))

