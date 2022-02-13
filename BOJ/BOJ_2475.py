# Baekjoon Online Judge - 2475번. 검증수

numbers = list(map(int, input().split()))
result = 0
for num in numbers:
    result += (num ** 2)
print(result % 10)
