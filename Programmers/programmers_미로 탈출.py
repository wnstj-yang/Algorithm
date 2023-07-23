from collections import deque


def bfs(x, y, target, N, M, maps):
    q = deque()
    q.append((x, y, 0))
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    while q:
        x, y, cnt = q.popleft()
        # 매개변수로 받은 target('L' OR 'E')
        if maps[x][y] == target:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 'X'
            if not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
    # 못찾으면 -1을 반환해준다
    return -1


def solution(maps):
    answer = 0
    maps = [list(item) for item in maps]
    N, M = len(maps), len(maps[0])
    start = [0, 0]
    lever = [0, 0]
    # start와 lever가 있는 좌표들을 구한다
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start[0], start[1] = i, j
            elif maps[i][j] == 'L':
                lever[0], lever[1] = i, j
    start_to_lever = bfs(start[0], start[1], 'L', N, M, maps)
    lever_to_end = bfs(lever[0], lever[1], 'E', N, M, maps)
    # 둘 중 하나라도 -1이 나오면 도달하지 못한다
    if start_to_lever == -1 or lever_to_end == -1:
        return - 1
    # S -> L + L -> E까지의 최단거리들을 더한 값이 정답이다
    return start_to_lever + lever_to_end
