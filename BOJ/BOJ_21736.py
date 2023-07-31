# Baekjoon Online Judge - 21736번. 헌내기는 친구가 필요해

from collections import deque


def bfs(x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    cnt = 0 # 사람을 만난 명수
    # 이미 지나간 곳은 체크하지 않기 위해 visited 리스트를 활용
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나면 끝
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 다음 방문할 곳이 방문하지 않았고 벽이 아니라면
            if not visited[nx][ny] and board[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx, ny))
                # 사람이라면 명수 count
                if board[nx][ny] == 'P':
                    cnt += 1
    return cnt


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            result = bfs(i, j)
            break
if result == 0:
    print('TT')
else:
    print(result)

