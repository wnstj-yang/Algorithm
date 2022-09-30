# SW Expert Academy - 14413번. 격자판 칠하기

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    coors = []
    # '?'는 상관 없이 현재 '#'과 '.'의 좌표값들과 이를 활용한 홀짝으로 진행
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '?':
                coors.append((i, j))
    check = False
    # x + y가 짝수일 때 arr[x][y]가 '#'이라면, x + y가 홀수일 때는 arr[x][y]가 '.' 이여야 한다
    for x, y in coors:
        # x + y가 홀수일 때 '#'이라면 틀린 것
        if (x + y) % 2:
            if arr[x][y] == '#':
                check = True
                break
        # x + y가 짝수일 때 '.'이라면 틀린 것
        else:
            if arr[x][y] == '.':
                check = True
                break
    # 위의 과정이 틀렸다면 홀수와 짝수를 바꿔서 진행한다. 즉, x + y가 홀수일 때 arr[x][y]가 '.'이고, 짝수일 때 arr[x][y]가 '#'인 경우
    if check:
        check_2 = False
        for x, y in coors:
            # x + y가 홀수일 때 '.'이라면 틀린 것
            if (x + y) % 2:
                if arr[x][y] == '.':
                    check_2 = True
                    break
            # x + y가 짝수일 때 '#'이라면 틀린 것
            else:
                if arr[x][y] == '#':
                    check_2 = True
                    break
        if check_2:
            print('#{} impossible'.format(tc))
        else:
            print('#{} possible'.format(tc))

    else:
        print('#{} possible'.format(tc))
