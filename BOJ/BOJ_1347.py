# Baekjoon Online Judge - 1347번. 미로 만들기


N = int(input())
orders = input()
# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

path = [(0, 0)]
d = 1
x, y = 0, 0
for order in orders:
    if order == 'R':
        d = (d + 1) % 4
    elif order == 'L':
        d = (d - 1) % 4
    else:
        x = x + dx[d]
        y = y + dy[d]
        path.append((x, y))

# x, y의 최소, 최대값들을 구해서 만들어지는 미로 간격과 음수인 좌표값을 양수로 바꾸는데 활용
path.sort(key=lambda x: x[0])
min_x, max_x = path[0][0], path[-1][0]
path.sort(key=lambda x: x[1])
min_y, max_y = path[0][1], path[-1][1]

board = [['#' for _ in range(min_y, max_y + 1)] for _ in range(min_x, max_x + 1)]
# 기준을 0, 0으로 잡았기 때문에 음수인 좌표값들에 대해서 최소값을 구한것을 빼주면 양수로 만들어진다.
for i in range(len(path)):
    path[i] = (path[i][0] - min_x, path[i][1] - min_y)

for x, y in path:
    board[x][y] = '.'

for line in board:
    print(''.join(line))
