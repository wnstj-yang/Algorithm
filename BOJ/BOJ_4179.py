# Baekjoon Online Judge - 4179번. 불!

from collections import deque

# 4방향(수평, 수직)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, fire_list):
    global ans
    queue = deque()
    queue.append((a, b))
    result = 1

    # 최소 구했으면 ㅌㅌ
    check = False
    while queue:

        # 지훈이가 움직일 수 있는 공간의 길이만큼 순회
        length = len(queue)
        for i in range(length):
            x, y = queue.popleft()

            # 가장자리에 도착했다? 그럼 그게 최소니까 빠짐
            if x == 0 or x == R - 1 or y == 0 or y == C - 1:
                if maze[x][y] == 'J':
                    ans = result
                    return

            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                else:
                    if maze[nx][ny] == '.':
                        queue.append((nx, ny))
                        maze[nx][ny] = 'J'

        # result가 움직이는 거리
        result += 1

        # 불의 위치의 길이만큼 4방향 탐색
        f_length = len(fire_list)
        for _ in range(f_length):
            x, y = fire_list.popleft()
            for z in range(4):
                nx = x + dx[z]
                ny = y + dy[z]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                else:
                    # 벽이거나 불이면 check 안함
                    if maze[nx][ny] != '#' and maze[nx][ny] != 'F':
                        maze[nx][ny] = 'F'
                        fire_list.append((nx, ny))


R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]
ans = 'IMPOSSIBLE'
j_x, j_y = 0, 0
fire_list = deque()
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            j_x, j_y = i, j

        if maze[i][j] == 'F':
            fire_list.append((i, j))
bfs(j_x, j_y, fire_list)
print(ans)
