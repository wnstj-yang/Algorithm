# SW Expert Academy - 1966번. 숫자를 정렬하자

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print('#{} '.format(tc), end='')
    print(*numbers)
