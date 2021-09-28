# Baekjoon Online Judge - 20055번. 컨베이어 벨트 위의 로봇
from collections import deque
N, K = map(int, input().split())
belt = deque(map(int, input().split()))
# 내리는 위치일 때 벨트와 달리 로봇은 벨트에서 나간다
robot = deque([0] * N)

# 첫 단계
level = 1
# 1~4조건을 다 거친 후가 1단계임

while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    # 회전 했을 때 마지막에 로봇 내리는 위치는 내려져야 한다
    robot[-1] = 0

    # 2. 가장 먼저 올라간 로봇부터 이동 체크
    # 로봇이 존재하는지 확인
    if 1 in robot:
        # 가장 먼저 올라간 로봇부터 이동 체크 (내리는 위치 구분)
        for i in range(N-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
                robot[i+1] = 1
                belt[i+1] -= 1
                robot[i] = 0
            # 이동하고 나서 내리는 위치에 로봇이 있을 경우 내려준다
            if robot[-1] == 1:
                robot[-1] = 0
    # 로봇 올린다
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    # 내구도 체크
    if belt.count(0) >= K:
        break
    level += 1

print(level)


