# SW Expert Academy - 2382. [모의 SW 역량테스트] 미생물 격리


def move():
    global live_list
    live_dict = {}
    new_list = []
    for i in range(len(live_list)):
        x, y, cnt, direct = live_list[i]
        # 군집의 미생물 수가 0이면 진행 X
        if cnt == 0:
            continue
        nx = x + dx[direct]
        ny = y + dy[direct]
        # 약품 처리된 곳을 방문하게 될 시 미생물 수와 방향 변화
        if nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:
            live_list[i][2] = int(cnt / 2)
            live_list[i][3] = change_direct[direct]
        # 각 좌표값에 따라 군집들의 정보를 넣는다.(+ 한 곳에 만나지는지 체크한다)
        if (nx, ny) not in live_dict:
            live_dict[(nx, ny)] = [[live_list[i][2], live_list[i][3]]]
        else:
            live_dict[(nx, ny)].append([live_list[i][2], live_list[i][3]])

    # 이동 후의 군집 정보들을 바탕으로 새로운 군집 정보로 업데이트
    for key, value in live_dict.items():
        cnt, direct = 0, 0
        if len(value) >= 2:
            # 미생물 수로 정렬 후 방향과 미생물 수의 합을 구한다
            value.sort(key=lambda x:x[0], reverse=True)
            direct = value[0][1]
            for item in value:
                cnt += item[0]
        else:
            cnt = value[0][0]
            direct = value[0][1]
        # 군집의 미생물 수가 0이면 더이상 추가 X
        if cnt != 0:
            new_list.append([key[0], key[1], cnt, direct])
    # 새로 만들어진 군집의 정보들을 업데이트
    live_list = new_list


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    change_direct = [0, 2, 1, 4, 3] # 반대 방향으로 바꿀 시 미리 인덱싱 설정
    live_list = [list(map(int, input().split())) for _ in range(K)] # 각 군집들의 정보
    answer = 0
    for _ in range(M):
        move()
    for item in live_list:
        answer += item[2]
    print('#{} {}'.format(tc, answer))

