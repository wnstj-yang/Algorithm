from collections import deque


def solution(maps):
    answer = -1
    N, M = len(maps), len(maps[0])
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0, 0, 1))
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, cnt = q.popleft()
        if x == N - 1 and y == M - 1:
            answer = cnt
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
                
    return answer