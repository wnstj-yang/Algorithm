# DFS/BFS - 유형별 문제. 블록 이동하기 355p

from collections import deque


def bfs(board):
    N = len(board)
    q = deque()
    q.append((0, 0, 0, 1, 0))
    visited = [{(0, 0), (0, 1)}]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x1, y1, x2, y2, time = q.popleft()
        if (x1 == N - 1 and y1 == N - 1) or (x2 == N - 1 and y2 == N - 1):
            return time

        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= N:
                continue
            if nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= N:
                continue
            if {(nx1, ny1), (nx2, ny2)} not in visited and (board[nx1][ny1] == 0 and board[nx2][ny2] == 0):
                q.append((nx1, ny1, nx2, ny2, time + 1))
                visited.append({(nx1, ny1), (nx2, ny2)})

        #  좌우에 있을 때 위 아래 대각선 모두 살펴본다(4방향)
        if x1 == x2:
            for i in [-1, 1]:
                nx1 = x1 + i
                nx2 = x2 + i
                if 0 <= nx1 < N and 0 <= nx2 < N and board[nx1][y2] == 0 and board[nx2][y1] == 0:
                    if {(nx1, y2), (x2, y2)} not in visited:
                        visited.append({(nx1, y2), (x2, y2)})
                        q.append((nx1, y2, x2, y2, time + 1))
                    if {(nx2, y1), (x1, y1)} not in visited:
                        visited.append({(nx2, y1), (x1, y1)})
                        q.append((nx2, y1, x1, y1, time + 1))
        # 상하인 경우에도 마찬가지로 대각선 모두 살펴봄(4방향)
        if y1 == y2:
            for i in [-1, 1]:
                ny1 = y1 + i
                ny2 = y2 + i
                if 0 <= ny1 < N and 0 <= ny2 < N and board[x1][ny1] == 0 and board[x2][ny2] == 0:
                    if {(x1, y1), (x1, ny1)} not in visited:
                        visited.append({(x1, y1), (x1, ny1)})
                        q.append((x1, y1, x1, ny1, time + 1))
                    if {(x2, ny2), (x2, y2)} not in visited:
                        visited.append({(x2, ny2), (x2, y2)})
                        q.append((x2, ny2, x2, y2, time + 1))


def solution(board):
    answer = bfs(board)
    return answer