# SW Expert Academy - 7584번. 자가 복제 문자열

T = int(input())

for tc in range(1, T + 1):
    K = int(input()) - 1
    # 4배수 혹은 2배수로 나와야 하므로 홀수인 경우 각각에 대한 조건으로 만들어준다
    while K >= 0:
        if K % 4 == 0:
            K = 0
            break
        if K % 2:
            K = (K - 1) // 2
        else:
            K = 1
            break
    print('#{} {}'.format(tc, K))
