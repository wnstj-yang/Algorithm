# SW Expert Academy - 10570번. 제곱 팰린드롬 수

T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())
    result = 0
    for i in range(A, B + 1):
        num = i ** 0.5
        if num.is_integer():
            original_num = list(str(int(i)))
            num = list(str(int(num)))
            if original_num == original_num[::-1]:
                if num == num[::-1]:
                    result += 1
    print('#{} {}'.format(tc, result))
