# Baekjoon Online Judge - 2638번. 치즈


from collections import deque


# 외부 공기와 비교를 위해 내부가 아니라면 2로 초기화 
def bfs(temp):
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))
    return temp


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0
while True:
    temp = [item[:] for item in board]
    board = bfs(board)
    cheeses = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cheeses += 1
                contact_air = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if board[nx][ny] == 2:
                        contact_air += 1
                if contact_air >= 2:
                    temp[i][j] = 0
    # 치즈가 존재한다면 tempㄹ르 board에 다시 넣고 지속
    if cheeses:
        board = [item[:] for item in temp]

    else:
        print(time)
        break
    time += 1

