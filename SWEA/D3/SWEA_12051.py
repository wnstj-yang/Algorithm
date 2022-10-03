# SW Expert Academy - 12051번. 프리셀 통계

T = int(input())

for tc in range(1, T + 1):
    N, P_D, P_G = map(int, input().split())
    # 3가지의 경우로 나누어지며, 전체 승확률이 100이라면 다른 것이 100이 아니라면 Broken
    # 전체 승확률이 0이면 나머지도 0, 그 이외의 경우는 값을 찾아나간다 이긴 수가 같은지
    if P_D != 100 and P_G == 100:
        print('#{} Broken'.format(tc))
    elif P_D != 0 and P_G == 0:
        print('#{} Broken'.format(tc))
    else:
        check = False
        for i in range(1, N + 1):
            # 여기서 81.0이 81과 같은지 비교할때 같다고 표현한다.
            if (P_D * i / 100) == (P_D * i // 100):
                check = True
                break
        if check:
            print('#{} Possible'.format(tc))
        else:
            print('#{} Broken'.format(tc))
