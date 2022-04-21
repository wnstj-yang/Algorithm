# Baekjoon Online Judge - 20058번. 마법사 상어와 파이어스톰
from collections import deque


# 모든 격자를 시계 방향으로 90도 회전
def degree_90(x, y, rotate_gap):
    # 부분 격자 크기만큼의 임시 리스트를 만든 후 값을 넣음
    temp = [[0] * rotate_gap for _ in range(rotate_gap)]
    for i in range(rotate_gap):
        for j in range(rotate_gap):
            temp[j][rotate_gap - i - 1] = A[x + i][y + j]

    # 만들어진 부분 격자를 다시 원 리스트인 A에 넣는다. (부분 격자 크기 만큼)
    for i in range(rotate_gap):
        for j in range(rotate_gap):
            A[x + i][y + j] = temp[i][j]


def rotate_90(gap):
    # 전체 크기만큼 순회하나 부분 격자의 크기만큼 띄워가면서 90도 회전을 진행한다.
    for i in range(0, 2 ** N, 2 ** gap):
        for j in range(0, 2 ** N, 2 ** gap):
            degree_90(i, j, 2 ** gap)


# 각 칸마다 3개 이상 얼음과 인접하지 않을 시 양을 하나씩 줄인다.(없다면 pass)
def check_ice():
    q = deque()
    for x in range(2 ** N):
        for y in range(2 ** N):
            cnt = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= 2 ** N or ny < 0 or ny >= 2 ** N:
                    continue
                if A[nx][ny] >= 1:
                    cnt += 1
            # 인접한 칸들 중 갯수가 3개 미만인 경우 큐에 넣는다
            if cnt < 3:
                q.append((x, y))
    # 큐에 있는 좌표값들을 0보다 큰 경우 얼음의 양을 1씩 줄인다.
    while q:
        x, y = q.popleft()
        if A[x][y] > 0:
            A[x][y] -= 1


# BFS를 통해 덩어리 체크
def check_ice_lands():
    islands = []
    visited = [[0] * (2 ** N) for _ in range(2 ** N)]
    for i in range(2 ** N):
        for j in range(2 ** N):
            # 방문하지 않고 얼음이 아닌 곳인 경우 덩어리의 시작
            if visited[i][j] == 0 and A[i][j] > 0:
                island = deque()
                island.append((i, j))
                visited[i][j] = 1
                cnt = 1
                while island:
                    x, y = island.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= 2 ** N or ny < 0 or ny >= 2 ** N:
                            continue
                        if visited[nx][ny] == 0 and A[nx][ny] > 0:
                            island.append((nx, ny))
                            visited[nx][ny] = 1
                            cnt += 1
                islands.append(cnt)
    return islands


N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(len(L)):
    # 부분 격자로 나누고 시계 방향으로 90도 돌린다.
    rotate_90(L[i])
    check_ice()
# 덩어리들 중 정렬해서 최대인 것을 체크
islands_result = check_ice_lands()
islands_result.sort(reverse=True)
sum_result = 0
for i in A:
    sum_result += sum(i)
print(sum_result)
if len(islands_result) == 0:
    print(0)
else:
    print(islands_result[0])
