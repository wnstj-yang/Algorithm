def move(x, y, d, cnt, board):
    H, W = len(board), len(board[0])  # 각 가로 세로
    direction = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}  # 상하좌우 방향
    rx, ry = -1, -1  # return할 좌표(즉, 이동한 이후의 결과 x, y 좌표 값)
    for i in range(1, cnt + 1):  # 주어진 칸만큼 이동하는 횟수
        nx = x + direction[d][0] * i  # 현재 받은 x 좌표에 반복하는 횟수를 곱해준다
        ny = y + direction[d][1] * i  # 현재 받은 y 좌표에 반복하는 횟수를 곱해준다
        # 격자 범위를 벗어나거나 이동했을 때 장애물이 존재한다면 이동할 수 없다는 [-1, 1] 좌표 값을 반환
        if nx < 0 or nx >= H or ny < 0 or ny >= W or board[nx][ny] == 'X':
            return [-1, -1]
        rx, ry = nx, ny  # 이동이 반복하면서 이동한 좌표 값 초기화
    return [rx, ry]


def solution(park, routes):
    answer = []
    board = [list(item) for item in park]  # 리스트로 변환해서 각 칸마다 값이 넣어지도록 격자판 생성
    s_x, s_y = 0, 0  # 시작점
    H, W = len(board), len(board[0])  # H: 세로 / W : 가로
    for i in range(H):
        for j in range(W):
            if board[i][j] == 'S':
                s_x, s_y = i, j  # 시작점 좌표
                break

    for coor in routes:
        order = coor.split(' ')  # 비어 있는 곳을 바탕으로 명령 리스트를 받음
        # s_x, s_y 시작점 x, y좌표, order[0] : 방향 / order[1]: 이동 칸 수
        result = move(s_x, s_y, order[0], int(order[1]), board)
        # 이동할 수 없는 것이 반환된다면 무시되고, 아니라면 갱신 시켜준다
        if result != [-1, -1]:
            s_x, s_y = result[0], result[1]
    answer = [s_x, s_y]  # 이동이 완료된 좌표값을 정답으로 처리
    return answer
