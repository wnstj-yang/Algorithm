# SW Expert Academy - 1288번. 새로운 불면증 치료법

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cnt = 1
    numbers = [0] * 10
    while True:
        for i in str(N * cnt):
            numbers[int(i)] += 1
        if 0 not in numbers:
            break
        cnt += 1
    print('#{} {}'.format(tc, N * cnt))
