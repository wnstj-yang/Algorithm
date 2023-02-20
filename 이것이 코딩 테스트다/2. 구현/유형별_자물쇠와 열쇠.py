def rotate(arr, M):
    temp = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            temp[j][M - i - 1] = arr[i][j]

    return temp


def check(board, N):
    for i in range(N, N * 2):
        for j in range(N, N * 2):
            if board[i][j] != 1:
                return True
    return False


def solution(key, lock):
    answer = True
    N = len(lock)
    M = len(key)
    board = [[0] * (N * 3) for _ in range(N * 3)]
    for i in range(N, N * 2):
        for j in range(N, N * 2):
            board[i][j] = lock[i - N][j - N]
    for _ in range(4):
        key = rotate(key, M)
        for i in range(N * 2):
            for j in range(N * 2):
                for x in range(M):
                    for y in range(M):
                        board[i + x][j + y] += key[x][y]

                if check(board, N):
                    return True

                for x in range(M):
                    for y in range(M):
                        board[i + x][j + y] -= key[x][y]

    return answer
