# SW Expert Academy - 10505번. 소득 불균형

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    avg = sum(numbers) / N
    result = 0
    for num in numbers:
        if num <= avg:
            result += 1
    print('#{} {}'.format(tc, result))


