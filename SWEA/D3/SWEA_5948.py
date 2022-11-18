# SW Expert Academy - 5948번. 새샘이의 7-3-5 게임

T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    sum_numbers = []
    for i in range(5):
        for j in range(i + 1, 6):
            for k in range(j + 1, 7):
                num = numbers[i] + numbers[j] + numbers[k]
                if num not in sum_numbers:
                    sum_numbers.append(num)
    sum_numbers.sort()
    print('#{} {}'.format(tc, sum_numbers[-5]))

