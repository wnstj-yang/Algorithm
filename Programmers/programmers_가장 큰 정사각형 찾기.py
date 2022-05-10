def solution(board):
    answer = 0
    dp = [[0] * len(board[0]) for _ in range(len(board))]
    # 각 첫 행과 열에 기존 값 저장
    for j in range(len(board[0])):
        dp[0][j] = board[0][j]

    for i in range(len(board)):
        dp[i][0] = board[i][0]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    # 마지막에 최대인 값을 구해서 반환 시 제곱 적용
    for i in dp:
        answer = max(answer, max(i))

    return answer ** 2
