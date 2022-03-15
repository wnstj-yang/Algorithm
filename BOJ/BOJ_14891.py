# Baekjoon Online Judge - 14891번. 톱니바퀴


def check_direction(N, d):
    state = [0] * 4
    state[N] = d # 정해진 톱니바퀴의 방향 설정
    # 정해진 톱니바퀴 기준 오른쪽으로
    for i in range(N, 3):
        if wheels[i][2] == wheels[i + 1][6]:
            break
        state[i + 1] = state[i] * -1 # 오른쪽 톱니바퀴의 방향을 반대로
    # 정해진 톱니바퀴 기준으로 왼쪽으로
    for i in range(N, 0, -1):
        if wheels[i][6] == wheels[i - 1][2]:
            break
        state[i - 1] = state[i] * -1 # 왼쪽 톱니바퀴의 방향을 반대로
    return state


wheels = []
for _ in range(4):
    wheels.append(list(map(int, input())))
K = int(input())
for _ in range(K):
    n, direction = map(int, input().split())
    # n번 톱니바퀴에서 오른쪽으로, 왼쪽으로 쭉 가서 바퀴 돌리기 판단
    # 1. 돌리기 전에 옆의 톱니바퀴 맞물린 부분에서 극이 같은지 다른지 판단
    # 2. 같으면 회전 X(왼쪽 혹은 오른쪽 방향으로 더 안감), 다르면 회전
    state = check_direction(n - 1, direction)
    for i in range(4):
        # 시계 방향으로 회전
        if state[i] == 1:
            wheels[i] = [wheels[i][7]] + wheels[i][:7]
        # 반시계 방향으로 회전
        elif state[i] == -1:
            wheels[i] = wheels[i][1:] + [wheels[i][0]]
print(wheels[0][0] + wheels[1][0] * 2 + wheels[2][0] * 4 + wheels[3][0] * 8)
