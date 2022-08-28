# Baekjoon Online Judge- 3058번. 짝수를 찾아라

T = int(input())

for _ in range(T):
    numbers = list(map(int, input().split()))
    min_val, even_sum = 987654321, 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
            min_val = min(min_val, num)
    print(even_sum, min_val)
