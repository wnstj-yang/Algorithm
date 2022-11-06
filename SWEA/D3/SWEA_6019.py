# SW Expert Academy - 6019번. 기차 사이의 파리

T = int(input())

for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)
    print('#{} {}'.format(tc, time * F))
