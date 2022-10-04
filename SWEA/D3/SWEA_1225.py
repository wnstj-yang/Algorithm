# SW Expert Academy - 1225번. [S/W 문제해결 기본] 7일차 - 암호생성기


for _ in range(10):
    N = int(input())
    numbers = list(map(int, input().split()))

    while True:
        check = False
        for i in range(1, 6):
            num = numbers.pop(0) - i
            if num <= 0:
                numbers.append(0)
                check = True
                break
            else:
                numbers.append(num)

        if check:
            print('#{} '.format(N), end='')
            print(*numbers)
            break

