# Baekjoon Online Judge - 11720번. 숫자의 합

N = int(input())
number = input()
result = 0

for i in number:
    result += int(i)
print(result)