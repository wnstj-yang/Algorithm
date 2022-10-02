# SW Expert Academy - 12741번. 두 전구

T = int(input())
result = []
for tc in range(T):
    X = [0] * 101
    Y = [0] * 101
    cnt = 0
    A, B, C, D = map(int, input().split())
    for i in range(A, B):
        X[i] = 1

    for j in range(C, D):
        Y[j] = 1

    for i in range(101):
        if X[i] == 1 and (X[i] == Y[i]):
            cnt += 1
    result.append(cnt)

# 시간초과로 인해 모두 모아서 출력
for tc in range(T):
    print('#{} {}'.format(tc + 1, result[tc]))
