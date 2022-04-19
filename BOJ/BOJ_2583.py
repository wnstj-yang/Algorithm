# Baekjoon Online Judge - 2583번. 영역 구하기

from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            else:
                # 영역에 연결되는 부분이 있다면 큐에 넣어주면서 갯수를 카운트해준다
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1
    return cnt


M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    # 직사각형이 왼쪽 아래부터 시작하기 때문에 이를 조정해준다
    for i in range(M - y2, M - y1):
        for j in range(x1, x2):
            board[i][j] = 1

# 조정한 이후 영역을 모두 순회하면서 빈 영역들의 갯수들을 카운트해서 리스트에 넣는다.
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            result = bfs(i, j)
            answer.append(result)
answer.sort()
print(len(answer))
print(*answer)
