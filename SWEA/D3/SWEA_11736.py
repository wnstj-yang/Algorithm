# SW Expert Academy - 11736번. 평범한 숫자

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0
    for i in range(1, N - 1):
        max_val, min_val = max(numbers[i-1:i+2]), min(numbers[i-1:i+2])
        if numbers[i] != max_val and numbers[i] != min_val:
            result += 1
    print('#{} {}'.format(tc, result))
