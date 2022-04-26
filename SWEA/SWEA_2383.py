# SW Expert Academy - 2383. [모의 SW 역량테스트] 점심 식사시간


def dfs(k):
    global answer
    if k == people_cnt:
        stair_1, stair_2 = [], []
        # 방문체크를 한 것을 바탕으로 1, 2번째 계단으로 향하는 사람들을 넣는다
        for i in range(k):
            if not visited[i]:
                stair_2.append(i)
            else:
                stair_1.append(i)
        # 각 계단으로 향하는 사람들이 정해지면 걸리는 시간들을 구한다.
        one_time = check_time(stair_1, 1)
        two_time = check_time(stair_2, 2)
        # 구하는 시간들 중 최댓값을 구하고, 각각의 조합에 따른 최소값을 업데이트한다.
        result = max(one_time, two_time)
        answer = min(answer, result)
        return
    # 유동적으로 사람들이 어느 계단으로 가는지 파악해서 정한다.
    visited[k] = True
    dfs(k + 1)
    visited[k] = False
    dfs(k + 1)


def check_time(stair, num):
    distances = []
    # 미리 구한 사람과 계단 간의 거리 중 num(각 계단 번호)에 따라 거리를 새로 저장
    if num == 1:
        for i in stair:
            distances.append(people_dist[i][0])
    else:
        for i in stair:
            distances.append(people_dist[i][1])
    distances.sort()
    time = 1
    wait_state, down_state = [], []
    K = board[stairs[num - 1][0]][stairs[num - 1][1]]
    while distances or wait_state or down_state:
        # 대기하는 사람이 존재하면 계단을 내려가게 만든다(3명이면 꽉찼으므로 시간 넘김)
        while wait_state:
            if len(down_state) == 3:
                break
            wait_state.pop(0)
            down_state.append(K)
        # 앞에서부터 pop을 진행하면 인덱싱이 꼬이기 때문에 뒤에서부터 진행하여 빼준다
        for i in range(len(down_state) - 1, -1, -1):
            down_state[i] -= 1
            if down_state[i] == 0:
                down_state.pop(i)
        # 위와 마찬가지 이유로 인덱싱 에러 방지
        for i in range(len(distances) - 1, -1, -1):
            if time == distances[i]:
                distances.pop(0)
                wait_state.append(1)
        time += 1
    return time


T = int(input())

for tc in range(1, T + 1):
    answer = 987654321
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stairs = []
    people_cnt = 0 # 사람 수
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people.append((i, j))
                people_cnt += 1
            if board[i][j] > 1:
                stairs.append((i, j))

    people_dist = []
    # 완전탐색을 진행하기 때문에 미리 각 2개의 계단과 사람 사이의 거리를 구한다.
    for i in range(len(people)):
        dist = [0] * 2
        dist[0] = abs(people[i][0] - stairs[0][0]) + abs(people[i][1] - stairs[0][1])
        dist[1] = abs(people[i][0] - stairs[1][0]) + abs(people[i][1] - stairs[1][1])
        people_dist.append(dist)

    visited = [False] * people_cnt
    dfs(0)

    print('#{} {}'.format(tc, answer))
