class Solution(object):
    def generateMatrix(self, n):
        board = [[0] * n for _ in range(n)]
        # 우하좌상
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, 0 # 현재 좌표
        board[x][y] = 1 # n이 최소 1이므로 초기화
        number = 2 # 넣을 숫자
        d = 0 # 방향(우하좌상 0 ~ 4)
        for _ in range(1, n * n):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] > 0:
                d = (d + 1) % 4
                nx = x + dx[d]
                ny = y + dy[d]
            board[nx][ny] = number
            x, y = nx, ny # 좌표 초기화
            number += 1
        return board
            