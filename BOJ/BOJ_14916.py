# Baekjoon Online Judge - 14916번. 거스름돈

N = int(input())
answer = 0
while N > 0:
    if N % 5 == 0:
        answer += N // 5
        break
    else:
        N -= 2
        if N >= 0:
            answer += 1
if N < 0:
    print(-1)
else:
    print(answer)
