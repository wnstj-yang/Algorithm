# SW Expert Academy - 1959번. 두 개의 숫자열


def calculate(a, b):
    max_sum = 0
    for i in range(len(a) - len(b) + 1):
        temp = 0
        for j in range(len(b)):
            temp += a[i + j] * b[j]
        max_sum = max(max_sum, temp)
    return max_sum


T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())
    a_nums = list(map(int, input().split()))
    b_nums = list(map(int, input().split()))
    result = 0
    if len(a_nums) > len(b_nums):
        result = calculate(a_nums, b_nums)
    else:
        result = calculate(b_nums, a_nums)
    print('#{} {}'.format(tc, result))
