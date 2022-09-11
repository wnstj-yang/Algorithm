# SW Expert Academy - 2071번 평균값 구하기

T = int(input())

for tc in range(1, T + 1):
    num_list = list(map(int, input().split()))
    print('#{} {:.0f}'.format(tc, sum(num_list) / 10))
