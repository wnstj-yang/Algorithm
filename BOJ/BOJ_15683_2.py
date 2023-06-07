# Baekjoon Online Judge - 15683번. 감시


def dfs(k, arr):
    global ans
    # k. 즉, cctv의 개수를 의미하며 길이만큼 dfs를 진행한 이후 검사
    if k == len(cctv_list):
        temp = [item[:] for item in board] # 2차원 리스트 복사방법 - deepcopy는 시간이 많이 걸린다
        cnt = 0 # 사각지대의 개수
        for j in range(k):
            x, y = cctv_list[j][0], cctv_list[j][1] # cctv 개수 순서대로 인덱스를 잡기 때문에 해당 x, y 좌표를 구한다.
            for d in arr[j]: # 현재 인덱스(cctv 카메라)에서 방향에 있는 개수
                c = 1 # c는 while문으로 현재 방향의 격자판 끝까지 가도록 만드낟.
                while True:
                    nx = x + dx[d] * c # 다음 x 좌표
                    ny = y + dy[d] * c # 다음 y 좌표
                    # 격자 범위를 벗어나거나 벽을 만난 경우 끝
                    if nx < 0 or nx >= N or ny < 0 or ny >= M or temp[nx][ny] == 6:
                        break
                    # 0이라면 cctv 범위에 들어오므로 #으로 초기화
                    if temp[nx][ny] == 0:
                        temp[nx][ny] = '#'
                    c += 1 # 현재 방향에 대해 길이를 늘린다

        for i in temp:
            cnt += i.count(0) # 사각지대에 있는 개수를 구한다
        ans = min(ans, cnt) # 전역 변수로 처리한 ans와 최소값을 비교하여 구한다
        return

    # 현재 cctv 번호를 기준으로 방향을 구한다(camera는 방향)
    for i in camera[cctv_list[k][2]]:
        arr.append(i) # 구한 방향을 넣고
        dfs(k + 1, arr) # dfs를 진행한 이후
        arr.pop() # 끝나면 마지막으로 저장된 값을 빼주고 그 이후의 값을 넣는다


# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 각 카메라에 대해 90도 돌린 상태의 방향들을 저장해놓는다
camera = [
    [],
    [[1], [2], [3], [0]],
    [[3, 1], [0, 2]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    [[0, 1, 2, 3]]
]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv_list = [] # 각 cctv의 좌표와 cctv의 번호를 저장
ans = 987654321
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv_list.append((i, j, board[i][j]))
dfs(0, [])
print(ans)

