# SW Expert Academy - 2112. [모의 SW 역량테스트] 보호 필름


def dfs(idx, count, target):
    global answer
    if count > answer:
        return

    if count == target:
        if check():
            answer = min(answer, count)
        return

    for i in range(idx, D):
        for k in range(W):
            board[i][k] = 0
        dfs(i + 1, count + 1, target)
        for k in range(W):
            board[i][k] = 1
        dfs(i + 1, count + 1, target)
        for k in range(W):
            board[i][k] = board2[i][k]


def check():
    for j in range(W):
        cnt = 1
        for i in range(D - 1):
            if cnt == K:
                break
            if board[i][j] == board[i + 1][j]:
                cnt += 1
            else:
                cnt = 1
        if cnt != K:
            return False
    return True


T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    answer = 987654321
    board = [list(map(int, input().split())) for _ in range(D)]
    board2 = [item[:] for item in board]
    if check():
        answer = 0
    else:
        for i in range(1, D + 1):
            dfs(0, 0, i)
            if answer < 987654321:
                break

    print('#{} {}'.format(tc, answer))
