# Baekjoon Online Judge - 5532번. 방학 숙제


L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

result = 0
while True:
    if A > 0 or B > 0:
        A -= C
        B -= D
        result += 1
    if A <= 0 and B <= 0:
        print(L - result)
        break
