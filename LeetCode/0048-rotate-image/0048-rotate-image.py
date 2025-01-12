class Solution(object):
    def rotate(self, matrix):
        N = len(matrix)
        # 1. 배열의 중간을 기준으로 위, 아래 교환
        for i in range(N // 2):
            for j in range(N):
                matrix[i][j], matrix[N - 1 - i][j] = matrix[N - 1 - i][j], matrix[i][j]
        # 2. 왼쪽 위 -> 오른쪽 아래 대각선 기준으로 각각 값 교환
        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

        