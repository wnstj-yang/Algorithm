# Baekjoon Online Judge - 3055번. 탈출
# 1. 물을 한번 채운다. 2. 두더지가 비버를 찾으려 한다 3. 1,2 반복

from collections import deque

# 비버찾기
def find_beaver(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        length = len(queue)
        for i in range(length):
            x, y = queue.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                else:
                    # 비버의 굴을 찾았다면 끝
                    if arr[nx][ny] == 'D':
                        print(visited[x][y])
                        return

                    # 방문하지 않고 비어있는 곳이라면 두더지가 움직일 수 있는 곳임
                    if visited[nx][ny] == 0 and arr[nx][ny] == '.':
                        queue.append((nx, ny))
                        # visited에다가 이동거리를 기록한다.
                        visited[nx][ny] = visited[x][y] + 1
        # 1분에 두더지가 이동을 했으니 다시 물로 채운다.
        fill_water()
    print('KAKTUS')
    return



def fill_water():
    w_length = len(water_list)
    for _ in range(w_length):
        x, y = water_list.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            else:
                # 비어있는 곳이면 물로 채운다.
                if arr[nx][ny] == '.':
                    arr[nx][ny] = '*'
                    water_list.append((nx, ny))


# 상하좌우 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
a, b = 0, 0
water_list = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            a = i
            b = j
        if arr[i][j] == '*':
            water_list.append((i, j))
# 물로 채우고 비어의 굴을 찾는다.
fill_water()
find_beaver(a, b)
