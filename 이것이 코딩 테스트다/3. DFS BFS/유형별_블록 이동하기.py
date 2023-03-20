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


def solution(board):
    answer = 0
    bfs(board)
    return answer