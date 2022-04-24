# Baekjoon Online Judge - 9663번. N-Queen


def dfs(x):
    global result
    if x == N:
        result += 1
        return

    for y in range(N):
        check = True
        board[x] = y # 퀸을 놓음
        for i in range(x):
            # 같은 열에 퀸이 있다면 지속 X, 왼쪽 위, 오른쪽 위 대각선의 좌표값을 빼고 절댓값을 했을 때 같다면 퀸이 존재하므로 지속 X
            # 위에서 아래로 채워나가기 때문에 아래 대각선 체크 X
            if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
                check = False
                break
        if check:
            dfs(x + 1)


N = int(input())
result = 0
# 2차원 리스트가 아니라 1차원 리스트로 인덱스가 행(x), 값이 열(y)로 파악
board = [0 for _ in range(N)]
dfs(0)
print(result)
