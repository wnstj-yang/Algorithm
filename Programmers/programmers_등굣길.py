def solution(m, n, puddles):
    board = [[0] * (m + 1) for _ in range(n + 1)]
    board[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            # 좌표 값이 [m, n]형태로 주어지므로 [j, i]
            if [j, i] not in puddles:
                board[i][j] = board[i - 1][j] + board[i][j - 1]

    return board[n][m] % 1000000007
