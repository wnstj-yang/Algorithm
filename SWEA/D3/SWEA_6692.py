# SW Expert Academy - 6692번. 다솔이의 월급 상자

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = 0
    for i in range(N):
        pi, xi = map(str, input().split())
        pi = float(pi)
        xi = int(xi)
        result += pi * xi
    print('#{} {:.6f}'.format(tc, result))


