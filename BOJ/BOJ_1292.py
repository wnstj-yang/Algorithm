# Baekjoon Online Judge - 1292번. 쉽게 푸는 문제

a, b = map(int, input().split())
numbers = [0]
cnt = 1
# 길이가 1000을 넘어서는 경우까지의 숫자를 구한다.
while True:
    if (cnt * (cnt + 1) // 2) > 1000:
        break
    cnt += 1
# 해당 숫자(cnt)까지의 i만큼 수를 저장
for i in range(cnt + 1):
    for j in range(i):
        numbers.append(i)
print(sum(numbers[a:b + 1]))
