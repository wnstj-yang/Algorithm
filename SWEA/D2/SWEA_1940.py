# SW Expert Academy - 1940번. 가랏! RC카!

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dist, vel = 0, 0
    for _ in range(N):
        info = list(map(int, input().split()))
        if info[0] == 0:
            dist += vel
        elif info[0] == 1:
            vel += info[1]
            dist += vel
        else:
            # 감속 시 현재 속도보다 크다면 0으로
            if vel < info[1]:
                continue
            vel -= info[1]
            dist += vel
    print('#{} {}'.format(tc, dist))
