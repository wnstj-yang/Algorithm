def solution(board):
    N = len(board)
    answer = 0
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    bombs = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                bombs.append((i, j))
    for x, y in bombs:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = 1
    for line in board:
        answer += line.count(0)
    return answer
