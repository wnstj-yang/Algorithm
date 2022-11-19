# Baekjoon Online Judge - 26041번. 비슷한 전화번호 표시


A = list(input().split())
B = input()
result = 0
for number in A:
    if number.startswith(B) and number != B:
        result += 1
print(result)
