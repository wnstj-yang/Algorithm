# SW Expert Academy - 1954번. 달팽이 숫자

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    num = 1
    x, y = 0, 0
    # 달팽이처럼 굴리되 각 방향마다 끝까지 가도록 만든다. 범위 설정 및 0인 경우에 값을 넣음 + 좌표 설정 중간중간 더하거나 빼야됨
    while num <= N ** 2:
        while y < N and arr[x][y] == 0:
            arr[x][y] = num
            num += 1
            y += 1
        x += 1
        y -= 1
        while x < N and arr[x][y] == 0:
            arr[x][y] = num
            num += 1
            x += 1
        x -= 1
        y -= 1
        while y >= 0 and arr[x][y] == 0:
            arr[x][y] = num
            num += 1
            y -= 1
        x -= 1
        y += 1
        while x >= 0 and arr[x][y] == 0:
            arr[x][y] = num
            num += 1
            x -= 1
        x += 1
        y += 1
    print('#{}'.format(tc))
    for line in arr:
        print(*line)