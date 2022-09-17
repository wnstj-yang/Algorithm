# SW Expert Academy - 1926번. 간단한 369게임

N = int(input())

for i in range(1, N + 1):
    num = str(i)
    check = True
    for i in num:
        if i in ['3', '6', '9']:
            print('-', end='')
            check = False
    if check:
        print(num, end=' ')
    else:
        print(end=' ')
