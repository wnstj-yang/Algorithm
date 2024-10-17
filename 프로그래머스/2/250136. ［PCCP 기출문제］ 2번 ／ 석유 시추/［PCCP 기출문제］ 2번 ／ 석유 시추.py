from collections import deque



def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)]
    values = {}
    num = 1
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] > 0:
                visited[i][j] = num
                q = deque()
                q.append((i, j))
                value = land[i][j] 
                cnt = 1
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if not visited[nx][ny] and land[nx][ny] == value:
                            cnt += 1
                            visited[nx][ny] = num
                            q.append((nx, ny))
                values[num] = cnt
                num += 1
    for j in range(m):
        selected = set()
        for i in range(n):
            if visited[i][j] > 0:
                selected.add(visited[i][j])
        total = 0
        for s in selected:
            total += values[s]
        answer = max(answer, total)
    return answer