# SW Expert Academy - 1945번. 간단한 소인수분해

T = int(input())
prime_nums = [2, 3, 5, 7, 11]
for tc in range(1, T + 1):
    N = int(input())
    result = [0] * 5
    # 큰 값부터 시작해서 나머지가 남지 않을 때 까지 값을 줄인다
    for i in range(4, -1, -1):
        while N % prime_nums[i] == 0:
            N = N // prime_nums[i]
            result[i] += 1
    print('#{}'.format(tc), end=' ')
    print(*result)
