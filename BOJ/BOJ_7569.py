# Baekjoon Online Judge - 7569번. 토마토

from collections import deque


M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
# 상하좌우 + 위, 아래 - 핵심포인트
dk = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
answer = 0
tomatoes = deque()
for k in range(H):
    for x in range(N):
        for y in range(M):
            if board[k][x][y] == 1:
                tomatoes.append((k, x, y))
                visited[k][x][y] = True

while True:
    length = len(tomatoes)
    for _ in range(length):
        k, x, y = tomatoes.popleft()
        for i in range(6):
            nk = k + dk[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nk < 0 or nk >= H:
                continue
            if not visited[nk][nx][ny] and board[nk][nx][ny] == 0:
                tomatoes.append((nk, nx, ny))
                board[nk][nx][ny] = 1
                visited[nk][nx][ny] = True

    # 토마를 익히면서 다음 턴에 익힐 토마토가 존재하면 턴 수 증가. 아니면 끝
    if tomatoes:
        answer += 1
    else:
        break

# 모두 익지 못한 경우를 찾아야 하고 찾았으면 -1 출력을 위해 끝낸다
for k in range(H):
    for x in range(N):
        for y in range(M):
            if board[k][x][y] == 0:
                answer = -1
                break
        if answer == -1:
            break
    if answer == -1:
        break
print(answer)
