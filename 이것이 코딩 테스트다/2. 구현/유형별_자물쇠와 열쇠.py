# 유형별 구현 A10. 518p - 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059


def rotate(key, M):
    temp = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            temp[j][M - i - 1] = key[i][j]

    return temp


def check(board, N):
    for i in range(N, N * 2):
        for j in range(N, N * 2):
            if board[i][j] != 1:
                return False
    return True


def solution(key, lock):
    N = len(lock)
    M = len(key)
    board = [[0] * (N * 3) for _ in range(N * 3)]
    for i in range(N):
        for j in range(N):
            board[i + N][j + N] = lock[i][j]
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

    return False