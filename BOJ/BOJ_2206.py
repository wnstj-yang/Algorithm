# Baekjoon Online Judge - 2206번. 벽 부수고 이동하기

# 1. 벽 부수고 이동한 거리가 최단
# 2. 안부수고 간 것이 더 이동거리가 짧은 경우
from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    # 3차원 리스트로 벽을 부순 상태의 방문과 부수지 않은 상태의 방문을 구분한다.
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[1][0][0] = 1
    min_val = []
    while queue:
        x, y, cnt = queue.popleft()
        # 도착했으면 min_val에 저장해서 추후에 비교한다.
        if x == N - 1 and y == M - 1:
            min_val.append(visited[cnt][x][y])
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                # cnt가 1이면 벽을 부술 수 있고, 해당 좌표 방문하지 않았으며 벽인 경우
                if cnt == 1 and arr[nx][ny] == 1 and visited[cnt][nx][ny] == 0:
                    queue.append((nx, ny, 0))
                    # 벽을 부수고 난 후의 방문 체크
                    visited[0][nx][ny] = visited[cnt][x][y] + 1
                    continue
                # 그 외의 경우(cnt상관 없이 벽이 아닐 때)
                if visited[cnt][nx][ny] == 0 and arr[nx][ny] == 0:
                    queue.append((nx, ny, cnt))
                    visited[cnt][nx][ny] = visited[cnt][x][y] + 1

    return min_val


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
ans = bfs()

# 최단경로를 구하지 못하면 -1출력
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))

