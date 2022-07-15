from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board):
    q = deque()
    N = len(board)
    q.append((0, 0, 0, 1, 0))
    # 파이썬에서 set형식으로 저장할 시 {(0, 0), (0, 1)}과 {(0, 1), (0, 0)}을 같다고 본다.
    # 해당 처리를 안할 경우 테스트케이스 하나에서 시간 초과 및 시간이 길어진다.
    # 순서대로 좌표를 넣다보니 중복해서 넣을 수 있기 때문에 느릴 수 있다.
    visited = [{(0, 0), (0, 1)}]

    while q:
        x1, y1, x2, y2, time = q.popleft()
        if (x1 == N - 1 and y1 == N - 1) or (x2 == N - 1 and y2 == N - 1):
            return time

        # 상하좌우로 움직이기
        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= N:
                continue
            if nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= N:
                continue
            if {(nx1, ny1), (nx2, ny2)} not in visited and (board[nx1][ny1] == 0 and board[nx2][ny2] == 0):
                visited.append({(nx1, ny1), (nx2, ny2)})
                q.append((nx1, ny1, nx2, ny2, time + 1))

        # 로봇이 가로로 있을 때
        if x1 == x2:
            # 회전 시 로봇 좌표들의 위 혹은 아래에 둘 다 0으로 있어야 한다.
            for i in [-1, 1]:
                nx1 = x1 + i
                nx2 = x2 + i
                if (0 <= nx1 < N and 0 <= nx2 < N) and (board[nx1][y1] == 0 and board[nx2][y2] == 0):
                    if {(x1, y1), (nx1, y1)} not in visited:
                        visited.append({(x1, y1), (nx1, y1)})
                        q.append((x1, y1, nx1, y1, time + 1))
                    if {(x2, y2), (nx2, y2)} not in visited:
                        visited.append({(x2, y2), (nx2, y2)})
                        q.append((x2, y2, nx2, y2, time + 1))

        # 로봇이 세로로 있을 때
        elif y1 == y2:
            # 회전 시 로봇 좌표들의 좌 혹은 우에 둘 다 0으로 있어야 한다.
            for i in [-1, 1]:
                ny1 = y1 + i
                ny2 = y2 + i
                if (0 <= ny1 < N and 0 <= ny2 < N) and (board[x1][ny1] == 0 and board[x2][ny2] == 0):
                    if {(x1, y1), (x1, ny1)} not in visited:
                        visited.append({(x1, y1), (x1, ny1)})
                        q.append((x1, y1, x1, ny1, time + 1))
                    if {(x2, y2), (x2, ny2)} not in visited:
                        visited.append({(x2, y2), (x2, ny2)})
                        q.append((x2, y2, x2, ny2, time + 1))


def solution(board):
    answer = 0
    # 각 두 좌표값에서 이동 bfs
    answer = bfs(board)
    return answer
