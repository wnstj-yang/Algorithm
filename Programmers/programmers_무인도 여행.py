# 무인도 여행

from collections import deque


def solution(maps):
    board = [list(item) for item in maps]
    N, M = len(board), len(board[0])
    visited = [[False] * M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = []
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] != 'X':
                visited[i][j] = True
                cnt = int(board[i][j])
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue
                        if not visited[nx][ny] and board[nx][ny] != 'X':
                            cnt += int(board[nx][ny])
                            visited[nx][ny] = True
                            q.append((nx, ny))
                if cnt:
                    answer.append(cnt)
    if answer:
        answer.sort()
    else:
        answer = [-1]
    return answer
