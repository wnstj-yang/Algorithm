# SW Expert Academy - 2072번. 홀수만 더하기

T = int(input())

for tc in range(1, T + 1):
    odd_list = list(map(int, input().split()))
    result = 0
    for num in odd_list:
        if num % 2:
            result += num
    print('#{} {}'.format(tc, result))
