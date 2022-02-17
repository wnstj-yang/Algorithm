from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 2배로 범위를 늘린 이유는 파여있는 부분에서 움직일 때 유의함을 위함이다.
    # 예를 들어, (3, 5) -> (3, 6)으로 그림 상으로는 갈 수없는데 좌표 상으로 범위를 그대로하면
    # 접근 할 수가 있기 때문에 이를 2배로 늘려주는 스킬을 적용한다.
    area = [[0] * 101 for _ in range(101)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[-1] * 101 for _ in range(101)]
    # 마찬가지로 범위를 2배 늘렸으니 시작점, 아이템 위치도 늘려준다
    cX, cY, iX, iY = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY
    # 1. 해당 직사각형들을 1로 초기화 해준다
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        for i in range(2 * x1, 2 * x2 + 1):
            for j in range(2 * y1, 2 * y2 + 1):
                area[i][j] = 1
    # 2. 겹치는 부분 즉, 테두리만 남기기 위해 안의 값들을 0으로 다시 초기화를 한다.
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        for i in range(2 * x1 + 1, 2 * x2):
            for j in range(2 * y1 + 1, 2 * y2):
                area[i][j] = 0
    # 가장 짧은 경로를 구하기 때문에 BFS로 적용한다.
    q = deque()
    q.append((cX, cY))
    visited[cX][cY] = 0
    while q:
        x, y = q.popleft()
        # 2배로 늘렸으니 정답은 2로 줄여서 정한다.
        if x == iX and y == iY:
            answer = visited[x][y] // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:
                continue
            if area[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return answer
