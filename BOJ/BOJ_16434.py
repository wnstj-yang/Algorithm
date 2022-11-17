# Baekjoon Online Judge - 16434번. 드래곤 앤 던전

N, H_atk = map(int, input().split())
H_max, H_cur = 0, 0
for i in range(N):
    t, a, h = map(int, input().split())
    if t == 1:
        cnt = h % H_atk
        attacked = 0
        # 몬스터 입장에서 용사가 먼저 때리기 때문에
        # 나머지가 남으면 : 몬스터 공격은 cnt
        # 남지 않으면 : 몬스터 공격은 cnt - 1
        if cnt == 0:
            attacked = a * (h // H_atk - 1)
        else:
            attacked = a * (h // H_atk)
        H_cur = H_cur - attacked
    else:
        H_atk += a
        H_cur += h
    # 현재 체력이 0보다 크다면 최대 체력보다 커짐을 의미하여 0으로 초기화해준다
    # 예를 들어 현재 체력 : -6, 포션 방에서 체력 + 10을 적용하면 현재 체력이 4가 되는데
    # 이에 대한 의미가 최대 체력 6이 필요한데 양수가 되면 체력이 필요 없음을 뜻한다. 그렇기에 0으로 초기화
    if H_cur > 0:
        H_cur = 0
    # 공격당한 값을 바탕으로 최대체력을 구하기 때문에 값이 -이므로 이를 양수로 바꿔서 계산
    H_max = max(H_max, -H_cur)
# 1을 더해주는 이유는 계산 값이 모든 과정을 거쳤을 때 0이 되는 것으로 가정되어 있기 때문에 그에 따라 체력이 남아있는 상태로 보기 위해
# 1을 더해준다.
print(H_max + 1)
