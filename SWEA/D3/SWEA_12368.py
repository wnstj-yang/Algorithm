# SW Expert Academy - 12368번. 24시간

T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())
    print('#{} {}'.format(tc, (a + b )% 24))
