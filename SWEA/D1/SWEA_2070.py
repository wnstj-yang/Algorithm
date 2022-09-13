# SW Expert Academy - 2070번. 큰 놈, 작은 놈, 같은 놈


T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())
    if A > B:
        print('#{} >'.format(tc))
    elif A < B:
        print('#{} <'.format(tc))
    else:
        print('#{} ='.format(tc))
