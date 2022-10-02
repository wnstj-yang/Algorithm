# SW Expert Academy - 12004번. 구구단 1

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    check = False
    for a in range(1, 10):
        b = N // a
        if b < 10 and a * b == N:
            check = True
            break
    if check:
        print('#{} Yes'.format(tc))
    else:
        print('#{} No'.format(tc))