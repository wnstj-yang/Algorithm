from collections import deque


def bfs(x, y, room, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    visited[x][y] = True
    q.append((x, y, 0))
    while q:
        x, y, cnt = q.popleft()
        # 맨하튼 거리가 2까지 온 좌표라면 더이상 순회 X (2 이하까지이기 때문)
        if cnt == 2:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            # P이면 사람이 존재하므로 X
            if not visited[nx][ny] and room[nx][ny] == 'P':
                return True
            # 그 이외 O이면 탐색이 가능.
            elif not visited[nx][ny] and room[nx][ny] == 'O':
                q.append((nx, ny, cnt + 1))
    return False


def solution(places):
    answer = []
    for place in places:
        room = []
        for info in place:
            room.append(list(info))
        visited = [[False] * 5 for _ in range(5)]
        check = False
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    if bfs(i, j, room, visited):
                        check = True
                        break
            if check:
                break
        if check:
            answer.append(0)
        else:
            answer.append(1)

    return answer
