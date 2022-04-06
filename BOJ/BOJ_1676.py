# Baekjoon Online Judge - 1676번. 팩토리얼 0의 개수


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


N = int(input())
number = factorial(N)
answer = 0
while True:
    if number % 10 == 0:
        answer += 1
        number = number // 10
    else:
        break
print(answer)
