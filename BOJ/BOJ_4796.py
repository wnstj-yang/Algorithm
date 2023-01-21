# Baekjoon Online Judge - 4796번. 캠핑

idx = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    result = 0
    while V:
        if P <= V:
            result += L
            V -= P
        else:
            if V > L:
                result += L
            else:
                result += V
            break
    print('Case {}: {}'.format(idx, result))
    idx += 1
