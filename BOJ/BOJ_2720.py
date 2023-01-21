# Baekjoon Online Judge - 2720번. 세탁소 사장 동혁

T = int(input())
price = [25, 10, 5, 1]
for _ in range(T):
    cnt = [0, 0, 0, 0]
    cent = int(input())
    for i in range(4):
        c = cent // price[i]
        cnt[i] += c
        cent = cent % price[i]
    print(*cnt)
