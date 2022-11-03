# SW Expert Academy - 6190번. 정곤이의 단조 증가하는 수


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            num = numbers[i] * numbers[j]
            temp = str(num)
            check = True
            for k in range(len(temp) - 1):
                if int(temp[k + 1]) < int(temp[k]):
                    check = False
                    break
            if check:
                result = max(result, num)
    if result == 0:
        result = -1
    print('#{} {}'.format(tc, result))

