# Baekjoon Online Judge - 1731번. 추론

N = int(input())
numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)
d = 0 # 등차
r = 0 # 등비
if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
    d = numbers[1] - numbers[0]
if d == 0:
    r = numbers[1] // numbers[0]
    print(numbers[-1] * r)
else:
    print(numbers[-1] + d)
