# SW Expert Academy - 1986번. 지그재그 숫자

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = 0
    for i in range(1, N + 1):
        if i % 2:
            result += i
        else:
            result -= i
    print('#{} {}'.format(tc, result))
