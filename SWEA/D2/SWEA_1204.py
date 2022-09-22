# SW Expert Academy - 1204번. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T = int(input())

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    result, max_cnt = 0, 0
    for i in range(101):
        cnt = numbers.count(i)
        if max_cnt <= cnt:
            max_cnt = cnt
            result = i
    print('#{} {}'.format(N, result))
