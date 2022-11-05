# SW Expert Acadmey - 5656번. [모의 SW 역량테스트] 벽돌 깨기

from collections import deque


def dfs(t, arr):
    global answer
    if t == N:
        result = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j]:
                    result += 1
        answer = min(answer, result)
        return

    # 행 순부터 시작하면 원하는 방식대로 구슬이 순서대로 떨어지지 않게 된다.
    # 문제 예시의 경우 각 열마다 맨 위의 값이 있으면 구슬을 떨어트리고 그다음으로 넘어가는데,
    # 다시 맨 앞으로 돌아와 구슬이 떨어지므로 맞지 않는 방법
    # 그래서 열부터 시작해서 파고들게 한다. 되돌아오면 break로 다음 열로 넘어가게 함
    for j in range(W):
        for i in range(H):
            if arr[i][j]:
                q = deque()
                q.append((i, j, arr[i][j]))
                arr2 = [item[:] for item in arr]
                while q:
                    x, y, cnt = q.popleft()
                    if cnt == 1:
                        arr[x][y] = 0
                    else:
                        arr[x][y] = 0
                        for k in range(1, cnt):
                            for z in range(4):
                                nx = x + dx[z] * k
                                ny = y + dy[z] * k
                                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                                    continue
                                if arr[nx][ny] != 0 and (nx, ny, arr[nx][ny]) not in q:
                                    q.append((nx, ny, arr[nx][ny]))

                # 0으로 초기화된 리스트에 각 열마다 temp에 0이 아닌 값들을 저장한다.
                # 이후 맨 아래에서부터 값을 채워나감
                arr3 = [[0] * W for _ in range(H)]
                temp = [[] for _ in range(W)]

                for b in range(W):
                    for a in range(H - 1, -1, -1):
                        if arr[a][b]:
                            temp[b].append(arr[a][b])
                y = 0
                for item in temp:
                    x = H - 1
                    for num in item:
                        arr3[x][y] = num
                        x -= 1
                    y += 1

                dfs(t + 1, arr3)
                arr = arr2
                break


T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    answer = 987654321
    dfs(0, board)
    # 예외처리 부분 => 구슬을 다 떨어트리지 못한 경우?에 벽돌이 다 0이라면 답이 0임.
    if answer == 987654321:
        answer = 0
    print('#{} {}'.format(tc, answer))
