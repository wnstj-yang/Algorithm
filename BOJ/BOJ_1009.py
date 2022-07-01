# Baekjoon Online Judge - 1009번. 분산처리

T = int(input())
# 1 ~ 10까지 반복되는 수가 존재한다.
for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [4, 9]:
        if b % 2 == 0:
            print(a ** 2 % 10)
        else:
            print(a)
    elif a in [2, 3, 7, 8]:
        if b % 4 == 0:
            print(a ** 4 % 10)
        else:
            b = b % 4
            print(a ** b % 10)

