# SW Expert Academy - 14692번. 통나무 자르기

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 2로 나머지를 한 것이 두 조각으로 나누는 것이다. 이 때 1이 남으면 Bob이 이기고, 0이 되면 Alice가 이긴다
    # N = 2일 때 나무 조각이 각각 1로 만들어져 Bob차례에서 더 이상 나눌 수 없다. 그래서 Alice가 이긴다
    # N = 3일 때 나무 조각이 1, 2로 나누어져서 2가 남기 때문에 Bob 차례에서 한 번 더 나눌 수 있어서 Alice차례일 때 
    # 자를 수 없어서 Bob이 이긴다.
    if N % 2:
        print('#{} Bob'.format(tc))
    else:
        print('#{} Alice'.format(tc))
