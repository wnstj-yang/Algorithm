# SW Expert Academy - 4698번. 테네스의 특별한 소수


T = int(input())
prime_numbers = [False] * 1000001
for i in range(2, 1000001):
    if not prime_numbers[i]:
        for j in range(i * i, 1000001, i):
            prime_numbers[j] = True

for tc in range(1, T + 1):
    D, A, B = map(int, input().split())
    result = 0
    for i in range(A, B + 1):
        if not prime_numbers[i] and i > 1:
            if str(D) in str(i):
                result += 1
    print('#{} {}'.format(tc, result))