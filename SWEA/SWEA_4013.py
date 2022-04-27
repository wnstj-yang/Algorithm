# SW Expert Academy - 4013. [모의 SW 역량테스트] 특이한 자석

# 각 4개의 자석에서 현재 자석을 기준으로 방향을 구한다.
def find_direct(current, move):
    direct_list = [0] * 4
    direct_list[target - 1] = move
    # 현재 자석을 기준으로 오른쪽으로 방향 판단 진행
    for i in range(current, 3):
        if magnet[i][2] != magnet[i + 1][6]:
            direct_list[i + 1] = direct_list[i] * -1
        # 같은 것이 있다면 더이상 진행 X
        else:
            break
    # 현재 자석을 기준으로 왼쪽으로 자석들과의 방향 판단 진행
    for i in range(current, 0, -1):
        if magnet[i][6] != magnet[i - 1][2]:
            direct_list[i - 1] = direct_list[i] * -1
        else:
            break
    return direct_list


T = int(input())

for tc in range(1, T + 1):
    K = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    answer = 0
    for _ in range(K):
        target, move = map(int, input().split())
        direct = find_direct(target - 1, move)

        for i in range(4):
            # 1이면 시계방향, -1이면 시계 반대방향
            if direct[i] == 1:
                magnet[i] = [magnet[i][7]] + magnet[i][:7]
            elif direct[i] == -1:
                magnet[i] = magnet[i][1:] + [magnet[i][0]]
    answer = magnet[0][0] * 1 + magnet[1][0] * 2 + magnet[2][0] * 4 + magnet[3][0] * 8
    print('#{} {}'.format(tc, answer))
