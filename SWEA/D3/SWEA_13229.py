# SW Expert Academy - 13229번. 일요일

days = {
    'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4,
    'THU': 3, 'FRI': 2, 'SAT': 1
}


T = int(input())

for tc in range(1, T + 1):
    S = input()
    print('#{} {}'.format(tc, days[S]))
