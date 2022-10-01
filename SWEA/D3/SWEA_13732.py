# SW Expert Academy - 13732번. 정사각형 판정

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    wall_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                wall_list.append((i, j))
    sx, sy = wall_list[0][0], wall_list[0][1]
    ex, ey = wall_list[-1][0], wall_list[-1][1]
    # 맨 앞과 맨 끝의 좌표의 x, y를 빼서 같다면 정사각형일 수 있는 가능성 존재
    if ex - sx == ey - sy:
        check = False
        # 맨 앞과 끝의 범위를 돌면서 안의 내용 마저 '#'으로 채워져 있는지 확인하고, 아니라면 끝
        for i in range(sx, ex + 1):
            for j in range(sy, ey + 1):
                if arr[i][j] != '#':
                    check = True
                    break
            if check:
                break
        if check:
            print('#{} no'.format(tc))
        else:
            print('#{} yes'.format(tc))
    else:
        print('#{} no'.format(tc))
