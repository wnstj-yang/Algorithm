# SW Expert Academy - 3431번. 준환이의 운동관리

T = int(input())

for tc in range(1, T + 1):
    L, U, X = map(int, input().split())
    if L <= X <= U:
        print('#{} {}'.format(tc, 0))
    elif X > U:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, L - X))
