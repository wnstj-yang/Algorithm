# SW Expert Academy - [모의 SW 역량테스트] 줄기세포배양

T = int(input())
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    # N, M에 K시간만큼의 크기에 넉넉히 메모리를 더준다.
    board = [[0]*(M+K*2) for _ in range(N+K*2)]
    q = []
    temp = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 앞의 값은 시간, 뒤에거는 생명력으로 활용
            if temp[i][j] > 0:
                board[K+i][K+j] = [temp[i][j], temp[i][j]]
                q.append((K+i, K+j))
    # 0: 비활성 / 1: 활성/ 2: 죽은 상태
    for _ in range(K):
        length = len(q)
        temp_q = []
        for idx in range(length):
            x, y = q[idx]
            # 비활성 상태이면 시간 줄임
            if board[x][y][0] > 0:
                board[x][y][0] -= 1
            # 활성 상태일 때
            elif board[x][y][0] == 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 넉넉히 주어서 범위 벗어날 일이 없다.
                    # 줄기세포가 없다면 임시 큐에 저장해준다
                    if board[nx][ny] == 0:
                        temp_q.append((nx, ny, board[x][y][1]))
                # 세포 시간 및 생명력 감소
                board[x][y][0] -= 1
                board[x][y][1] -= 1
            else:
                # 시간이 지나도 생명력은 감소
                if board[x][y][1] > 0:
                    board[x][y][1] -= 1
        # 새로운 임시 큐의 값을 판단
        while temp_q:
            x, y, val = temp_q.pop(0)
            # 비어있으면 추가 (번식)
            if board[x][y] == 0:
                board[x][y] = [val, val]
                q.append((x, y))
            else:
                # 2개 이상이 한 곳에 번식하려고 할 때 생명력이 큰 것을 기준으로 넣는다
                if board[x][y][1] < val:
                    board[x][y] = [val, val]
    result = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            # 비어있으면 넘어간다
            if board[i][j] == 0:
                continue
            # 생명력으로 비활성, 활성상태 확인
            if board[i][j][1] > 0:
                result += 1
    print('#{} {}'.format(t, result))
