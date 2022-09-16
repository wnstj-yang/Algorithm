# SW Expert Academy - 2056번. 연월일 달력

T = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T + 1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    if int(year) < 0:
        print('#{} -1'.format(tc))
        continue

    if int(month) <= 0 or int(month) > 12:
        print('#{} -1'.format(tc))
        continue

    if int(day) > days[int(month)]:
        print('#{} -1'.format(tc))
        continue

    print('#{} {}/{}/{}'.format(tc, year, month, day))
