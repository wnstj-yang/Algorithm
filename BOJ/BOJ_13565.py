# Baekjoon Online Judge - 13565번. 침투

from collections import deque

# 상하좌우 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            else:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    # 안쪽까지 왔다면 끝임
                    if nx == M - 1:
                        return 'YES'
    return 'NO'


M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ans = 'NO'
# 바깥쪽에 흰색격자인 경우에 전류가 흐르므로 이에 대한 것만 check
# 방문 표시를 통해 이어져 있는 부분까지 처리
for i in range(N):
    if arr[0][i] == 0 and visited[0][i] == 0:
        ans = bfs(0, i)
        if ans == 'YES':
            break
print(ans)
