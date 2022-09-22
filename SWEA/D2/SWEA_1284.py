# SW Expert Academy - 1284번. 수도 요금 경쟁

T = int(input())

for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    B = 0
    if W <= R:
        B = Q
    else:
        B = Q + (W - R) * S
    print('#{} {}'.format(tc, min(A, B)))
