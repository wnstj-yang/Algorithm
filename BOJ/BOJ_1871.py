# Baekjoon Online Judge - 1871번. 좋은 자동차 번호판


N = int(input())

for _ in range(N):
    number = input()
    A, B = 0, int(number[4:])
    idx = 2
    for i in range(3):
        num = ord(number[i]) - 65
        A += num * (26 ** idx)
        idx -= 1
    if abs(A - B) <= 100:
        print('nice')
    else:
        print('not nice')