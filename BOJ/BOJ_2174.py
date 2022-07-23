# Baekjoon Online Judge - 2174번. 로봇 시뮬레이션

A, B = map(int, input().split())
N, M = map(int, input().split())
robots = [0]
board = [[0] * A for _ in range(B)]

# 동남서북 => 오른쪽, 왼쪽 90도 고려해서 1 혹은 -1을 적용했을 때 맞는지의 방향설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direc = {
    'E': 0, 'S': 1, 'W': 2, 'N': 3
}


for i in range(1, N + 1):
    x, y, d = map(str, input().split())
    # 일반적으로의 그래프 좌표로 변환
    x, y = B - int(y), int(x) - 1
    robots.append([x, y, direc[d]])
    board[x][y] = i

check = False
for _ in range(M):
    num, order, cnt = map(str, input().split())
    num = int(num)
    cnt = int(cnt)

    check = False
    if order == 'F':
        x, y, d = robots[num]
        for i in range(cnt):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= B or ny < 0 or ny >= A:
                print('Robot {} crashes into the wall'.format(num))
                check = True
                break
            else:
                if board[nx][ny]:
                    print('Robot {} crashes into robot {}'.format(num, board[nx][ny]))
                    check = True
                    break
                else:
                    board[x][y] = 0
                    board[nx][ny] = num
                    robots[num][0], robots[num][1] = nx, ny # 로봇의 상태변화도 적어야함
                    x, y = nx, ny
                    
    elif order == 'L':
        d = robots[num][2]
        robots[num][2] = (d - cnt) % 4
    else:
        d = robots[num][2]
        robots[num][2] = (d + cnt) % 4
    if check:
        break
if not check:
    print('OK')

