# SW Expert Academy - 11688번. Calkin-Wilf tree 1

T = int(input())

for tc in range(1, T + 1):
    seq = input()
    a, b = 1, 1
    for order in seq:
        if order == 'L':
            b = a + b
        else:
            a = a + b
    print('#{} {} {}'.format(tc, a, b))
