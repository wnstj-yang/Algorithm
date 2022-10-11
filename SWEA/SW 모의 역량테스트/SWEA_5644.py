# SW Expert Academy - 5644번. [모의 SW 역량테스트] 무선 충전


T = int(input())
# 정지, 상우하좌
dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]

for tc in range(1, T + 1):
    board = [[[] for _ in range(10)] for _ in range(10)]

    M, A = map(int, input().split())
    user_A = [0] + list(map(int, input().split()))
    user_B = [0] + list(map(int, input().split()))
    A_y, A_x = 0, 0
    B_y, B_x = 9, 9
    result = 0
    for a in range(A):
        y, x, c, p = map(int, input().split())
        y -= 1
        x -= 1
        # 위에서 아래
        k = 0
        # 충전 범위 좌표를 기준을 포함하여 상단에 범위를 칠해준다
        for j in range(y - c, y + 1):
            for i in range(x - k, x + k + 1):
                if j < 0 or j >= 10 or i < 0 or i >= 10:
                    continue
                board[i][j].append([p, a])
            k += 1
        # 충전 범위 좌표를 기준으로 하단에 범위를 칠해준다
        k = c - 1
        for j in range(y + 1, y + c + 1):
            for i in range(x - k, x + k + 1):
                if j < 0 or j >= 10 or i < 0 or i >= 10:
                    continue
                board[i][j].append([p, a])
            k -= 1

    # 각각 최대 값을 맨 앞으로 두기 위해 정렬을 진행해준다
    for j in range(10):
        for i in range(10):
            if len(board[i][j]) > 1:
                board[i][j].sort(key=lambda x:x[0], reverse=True)

    for i in range(len(user_A)):
        A_y = A_y + dy[user_A[i]]
        A_x = A_x + dx[user_A[i]]
        B_y = B_y + dy[user_B[i]]
        B_x = B_x + dx[user_B[i]]
        # A 위치에 충전 가능 / B 위치에 충전 X
        if board[A_y][A_x] and not board[B_y][B_x]:
            result += board[A_y][A_x][0][0]

        # A 위치에 충전 X / B 위치에 충전 가능
        elif not board[A_y][A_x] and board[B_y][B_x]:
            result += board[B_y][B_x][0][0]

        # A 위치에 충전 가능 / B 위치에 충전 가능
        elif board[A_y][A_x] and board[B_y][B_x]:
            # 같은 충전 범위에 있을 때
            if board[A_y][A_x][0][1] == board[B_y][B_x][0][1]:
                # A 위치의 충전 범위가 2개 이상이고 B 위치의 충전 범위가 1개 일 때 / B의 최대 + A의 2번째 최대
                if len(board[A_y][A_x]) > 1 and len(board[B_y][B_x]) == 1:
                    result += (board[A_y][A_x][1][0] + board[B_y][B_x][0][0])
                # A 위치의 충전 범위가 1개이고 B 위치의 충전 범위가 2개 이상일 때 / B의 2번째 최대 + A의 최대
                elif len(board[A_y][A_x]) == 1 and len(board[B_y][B_x]) > 1:
                    result += (board[A_y][A_x][0][0] + board[B_y][B_x][1][0])
                # A, B 위치 모두 같은 곳에 있을 때 나눠서 하는 조건이나 2명이기 때문에 그냥 한 번 더해준다
                elif len(board[A_y][A_x]) == 1 and len(board[B_y][B_x]) == 1:
                    result += board[A_y][A_x][0][0]
                # A, B 위치 모두 2개 이상인 경우에는 하나는 최대, 나머지 2개 중 최대 인 것을 더해준다
                else:
                    result += (board[A_y][A_x][0][0] + max(board[A_y][A_x][1][0], board[B_y][B_x][1][0]))
            # 서로 다른 충전 범위라면 각자 제일 큰 값을 더해준다
            else:
                result += (board[A_y][A_x][0][0] + board[B_y][B_x][0][0])
    print('#{} {}'.format(tc, result))
