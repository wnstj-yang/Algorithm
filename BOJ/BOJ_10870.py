# Baekjoon Online Judge - 10870번. 피보나치 수 5

# 재귀

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


N = int(input())
print(fibo(N))
