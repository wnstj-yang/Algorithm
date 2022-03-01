# Baekjoon Online Judge - 11050번. 이항 계수 1


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


N, K = map(int, input().split())
# n!/k!(n-k)!
print(factorial(N) // (factorial(K) * factorial(N - K)))
