# Baekjoon Online Judge - 12931번. 두 배 더하기


# 홀수를 보게 되면 1을 빼주고, 모두가 짝수라면 2로 다 나누어준다

N = int(input())
B = list(map(int, input().split()))
result = 0
while sum(B) != 0:
    check = True
    for i in range(len(B)):
        if B[i] % 2:
            B[i] -= 1
            check = False
            break
    if check:
        for i in range(len(B)):
            B[i] = B[i] // 2
    result += 1
print(result)
