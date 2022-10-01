# SW Expert Academy - 13428번. 숫자 조작


def comb(idx, k):
    if k == 2:
        candis.append(list(candi))
        return

    for i in range(idx, len(N)):
        if not visited[i]:
            visited[i] = True
            candi[k] = i
            comb(i, k + 1)
            visited[i] = False


T = int(input())

for tc in range(1, T + 1):
    N = list(map(str, input()))
    max_val = int(''.join(N))
    min_val = int(''.join(N))
    # 한 자리만 바꾸는 것이므로 조합으로 구한다.
    visited = [False] * len(N)
    candi = [0] * 2
    candis = []
    comb(0, 0)
    for x, y in candis:
        # 해당 인덱스끼리 바꿔주고 다시 되돌리는 작업을 진행하면서 최대, 최소값을 각각 구해준다.
        N[x], N[y] = N[y], N[x]
        if N[0] == '0':
            N[x], N[y] = N[y], N[x]
            continue

        num = int(''.join(N))
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        N[x], N[y] = N[y], N[x]

    print('#{} {} {}'.format(tc, min_val, max_val))


