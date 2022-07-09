# Baekjoon Online Judge - 1145번. 적어도 대부분의 배수


numbers = list(map(int, input().split()))
min_num = min(numbers)
while True:
    cnt = 0
    for num in numbers:
        if min_num % num == 0:
            cnt += 1
    if cnt >= 3:
        print(min_num)
        break
    min_num += 1
