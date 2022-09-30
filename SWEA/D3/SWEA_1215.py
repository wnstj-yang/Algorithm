# SW Expert Academy - 1215번. [S/W 문제해결 기본] 3일차 - 회문1

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    result = 0
    # 가로
    for i in range(8):
        for j in range(8 - N + 1):
            target = ''
            for k in range(j, j + N):
                target += arr[i][k]
            if target == target[::-1]:
                result += 1
    # 세로
    for j in range(8):
        for i in range(8 - N + 1):
            target = ''
            for k in range(i, i + N):
                target += arr[k][j]
            if target == target[::-1]:
                result += 1

    print('#{} {}'.format(tc, result))
