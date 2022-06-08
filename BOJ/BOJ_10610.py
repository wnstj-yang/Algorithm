# Baekjoon Online Judge - 10610번. 30


N = list(map(str, input()))
N.sort(reverse=True)
N = int(''.join(N))
if N % 30 == 0:
    print(N)
else:
    print(-1)
