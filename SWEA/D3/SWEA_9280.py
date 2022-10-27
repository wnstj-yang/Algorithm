# SW Expert Academy - 9280번. 진용이네 주차타워

from collections import deque


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = 0
    R_i = []
    for _ in range(N):
        R_i.append(int(input()))
    W_i = [0]
    for _ in range(M):
        W_i.append(int(input()))
    waiting = deque()
    parked = [0] * N
    for _ in range(2 * M):
        is_parked = False
        num = int(input())
        if num > 0:
            for i in range(N):
                if parked[i] == 0:
                    parked[i] = num
                    is_parked = True
                    answer += R_i[i] * W_i[num]
                    break
            if not is_parked:
                waiting.append(num)
        else:
            idx = parked.index(-num)
            parked[idx] = 0
            if waiting:
                num = waiting.popleft()
                for i in range(N):
                    if parked[i] == 0:
                        parked[i] = num
                        answer += R_i[idx] * W_i[num]
                        break
    print('#{} {}'.format(tc, answer))
