# 경주로 건설 -  BFS돌면서 cost 카운트. visited배열로 각 위치에 대한 값을 넣어서 비교한다.

from collections import deque


def bfs(x, y, c, d, board, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    INF = 987654321
    visited = [[INF] * N for _ in range(N)]
    q = deque()
    q.append((x, y, c, d))
    visited[x][y] = 0
    while q:
        x, y, c, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if board[nx][ny] == 0:
                cost = 0
                if i == d:
                    cost = 100
                else:
                    cost = 600
                if cost + c < visited[nx][ny]:
                    visited[nx][ny] = cost + c
                    q.append((nx, ny, cost + c, i))
    return visited[-1][-1]


def solution(board):
    answer = 0
    # 첫 시작지점부터 아래, 오른쪽으로 지나가기 때문에 이 두가지에 대한 최솟값을 구한다.
    a = bfs(0, 0, 0, 1, board, len(board))
    b = bfs(0, 0, 0, 3, board, len(board))
    answer = min(a, b)
    return answer
