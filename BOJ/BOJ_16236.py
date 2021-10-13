# Baekjoon Online Judge - 16236번. 아기 상어
# 방문한 곳을 갱신해서 좀 더 쉽게 접근했어야 하는 포인트를 찾기가 어려웠다 
# 조건에 대한 분석을 잘해야함
from collections import deque


def bfs(x, y):
    q = deque()
    # 좌표와 거리(시간)를 추가한다.
    q.append((x, y, 0))
    fishes = []
    while q:
        x, y, time = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            else:
                # 방문했거나 물고기 크기가 크면 X
                if visited[nx][ny] == 1 or space[nx][ny] > baby_shark:
                    continue
                # 방문하지 않고 공간이 비어있지 않음(물고기 존재) + 크기가 작다면
                if visited[nx][ny] == 0 and space[nx][ny] != 0 and space[nx][ny] < baby_shark:
                    # 물고기 추가 ( 먹을 수 있는 좌표 )
                    fishes.append((nx, ny, time + 1))
                # 아기 상어 이동가능한 공간들
                q.append((nx, ny, time + 1))
                visited[nx][ny] = 1
    # 거리가 최소인 것을 먼저 택한다.
    # 최소인 것이 2개 이상일 경우에는 가장 위쪽, 여기서도 조건 충족이 2개 이상이면 가장 왼쪽 택
    if len(fishes) > 0:
        fishes.sort(key=lambda x: (x[2], x[0], x[1]))
        return fishes[0]
    # 물고기 없으면 False
    else:
        return False


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 크기가 같은 물고기는 먹을 수 없으나 지나갈 수 있음
baby_shark = 2
ans = 0
size = 0
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
s_x, s_y = 0, 0

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            s_x, s_y = i, j
            space[i][j] = 0

# 물고기를 먹으면 갱신을 한다.
# 움직일 수 있는 범위
while True:
    visited = [[0] * N for _ in range(N)]
    result = bfs(s_x, s_y)
    # 반환된 결과값이 False면 끝
    if not result:
        break
    # 시간 추가
    ans += result[2]
    # 크기 추가(물고기 하나 먹음)
    size += 1
    # 같다면 아기 상어 크기 증가
    if size == baby_shark:
        baby_shark += 1
        size = 0
    # 시작점 초기화
    s_x, s_y = result[0], result[1]
    # 물고기 먹은 곳 빈 공간으로 처리
    space[s_x][s_y] = 0
print(ans)
