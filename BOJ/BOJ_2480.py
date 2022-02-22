# Baekjoon Online Judge - 2480번. 주사위 세개

numbers = [0] * 7
dice = list(map(int, input().split()))
for i in dice:
    numbers[i] += 1
max_num = max(numbers)
max_idx = numbers.index(max_num)
if max_num == 3:
    print(10000 + max_idx * 1000)

elif max_num == 2:
    print(1000 + max_idx * 100)

if max_num == 1:
    for i in range(1, 7):
        if max_idx < i and numbers[i] == 1:
            max_idx = i
    print(100 * max_idx)
