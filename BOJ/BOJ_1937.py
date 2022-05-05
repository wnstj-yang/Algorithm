# Baekjoon Online Judge - 1937번. 욕심쟁이 판다


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
state = [[1] * N for _ in range(N)]
answer = 0
board_list = []
for i in range(N):
    for j in range(N):
        board_list.append((board[i][j], i, j))
# 순서대로 순회가 아닌 값이 큰 것부터 순회해서 상하좌우로 움직일 수 있는 칸이 몇인지 업데이트
board_list.sort(key=lambda x: x[0], reverse=True)

for num, x, y in board_list:
    connection = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] > num:
            connection.append(state[nx][ny])
    # 상하좌우로 움직일 수 있는 칸 수가 존재하면 그 칸의 값들 중 최대 값에 현재위치에서 더해주면서 업데이트 진행
    # state[x][y]가 1이여도 무방. 어차피 큰 값의 좌표부터 진행하기 때문.
    if len(connection) > 0:
        state[x][y] = max(connection) + state[x][y]
    if answer < state[x][y]:
        answer = state[x][y]
print(answer)
