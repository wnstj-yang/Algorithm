# Baekjoon Online Judge - 2576번. 홀수

total = 0
min_odd = 987654321
for i in range(7):
    num = int(input())
    if num % 2:
        total += num
        min_odd = min(min_odd, num)
if min_odd == 987654321:
    print(-1)
else:
    print(total)
    print(min_odd)
