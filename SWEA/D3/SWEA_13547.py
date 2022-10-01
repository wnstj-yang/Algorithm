# SW Expert Academy - 13547번. 팔씨름

T = int(input())

for tc in range(1, T + 1):
    results = input()
    wins = 0
    for result in results:
        if result == 'o':
            wins += 1
    if wins < 8:
        needs = 8 - wins
        if needs <= 15 - len(results):
            print('#{} YES'.format(tc))
        else:
            print('#{} NO'.format(tc))
    else:
        print('#{} YES'.format(tc))

