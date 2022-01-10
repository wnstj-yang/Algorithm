# Baekjoon Online Judge - 1010번. 다리 놓기
# 조합 이용

def f(n):
    val = 1
    for i in range(1, n + 1):
        val *= i
    return val


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # 조합 공식을 이용하여 다리를 지을 수 있는 경우의 수를 구한다
    result = f(M) // (f(N) * f(M-N))
    print(result)