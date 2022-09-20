# SW Expert Academy - 1984번. 중간 평균값 구하기

T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print('#{} {}'.format(tc, round(sum(numbers[1:-1]) / 8)))
