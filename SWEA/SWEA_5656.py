# SW Expert Academy - 5656. [모의 SW 역량테스트] 벽돌 깨기
# 구슬은 항상 맨위의 벽돌만 깨뜨린다
from collections import deque
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(n, arr):
    global result
    if n == N:
        cnt = 0
        for r in range(H):
            for c in range(W):
                if arr[r][c] > 0:
                    cnt += 1
        if result > cnt:
            result = cnt
        return
    for y in range(W):
        check = False
        for x in range(H):
            if arr[x][y] != 0:
                # 리스트 슬라이싱으로 복사
                arr2 = [item[:] for item in arr]
                q = deque()
                q.append((x, y, arr[x][y]))
                while q:
                    x, y, val = q.popleft()
                    # 값이 1이면 해당 위치만 제거
                    if val == 1:
                        arr[x][y] = 0
                    else:
                        arr[x][y] = 0
                        # 벽돌에 적힌 숫자 - 1만큼 제거
                        for i in range(1, val):
                            for j in range(4):
                                nx = x + dx[j] * i
                                ny = y + dy[j] * i
                                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                                    continue
                                else:
                                    # 중복 방지
                                    if arr[nx][ny] != 0 and (nx, ny, arr[nx][ny]) not in q:
                                        q.append((nx, ny, arr[nx][ny]))
                # 지워진 이후 이동
                # 0으로 다 초기화 한 이후에 이동한 수를 넣는다
                arr3 = [[0] * W for _ in range(H)]
                for b in range(W):
                    temp = []
                    for a in range(H):
                        if arr[a][b] != 0:
                            temp.append(arr[a][b])
                    # 해당 열의 마지막 행부터 위로 채워나간다
                    # temp의 순서 중요함. 즉, temp는 위에서부터 아래로 값을 넣음
                    # 그래서 마지막 값이 첫 값이다.
                    for z in range(len(temp)):
                        arr3[H-1-z][b] = temp.pop()
                check = True

            # check를 통해 해당 열에서 벽돌을 다 깨고 이후에 다음 열로 이동하게 만든다.
            if check:
                dfs(n+1, arr3)
                # 돌아왔을 때 이동하기 이전의 값을 넣는다
                arr = arr2
                # 해당 열에 맨 위부터 벽돌을 다 깼다면 다음 열로 이동하게 break
                break
    # 돌지 않았을 때
    if result == 987654321:
        dfs(N, arr)
T = int(input())

for t in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    result = 987654321
    dfs(0, board)
    print('#{} {}'.format(t, result))
