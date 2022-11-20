# SW Expert Academy - 5515번. 2016년 요일 맞추기

T = int(input())
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T + 1):
    now = 4
    m, d = map(int, input().split())
    days = 0
    for i in range(1, m):
        days += month[i]
    days += d
    print('#{} {}'.format(tc, (now + days - 1) % 7))
