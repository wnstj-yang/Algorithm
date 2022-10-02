# SW Expert Academy - 12221번. 구구단2

T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())
    if A >= 10 or B >= 10:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, A * B))
