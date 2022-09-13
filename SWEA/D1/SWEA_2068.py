# SW Expert Academy - 2068번. 최대수 구하기

T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, max(numbers)))
