# Baekjoon Online Judge - 25965번. 미션 도네이션

N = int(input())
for _ in range(N):
    M = int(input())
    result = 0
    missions = [list(map(int, input().split())) for _ in range(M)]
    k, d, a = map(int, input().split())
    for K, D, A in missions:
        temp = K * k + A * a - D * d
        if temp > 0:
            result += temp
    print(result)
