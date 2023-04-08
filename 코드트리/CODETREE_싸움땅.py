# 코드트리 - 싸움땅

# 코드 정리를 안했당..


def move_player(number):
    x, y, direc = players[number][0], players[number][1], players[number][2]
    nx = x + dx[direc]
    ny = y + dy[direc]
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        direc = (direc + 2) % 4
        nx = x + dx[direc]
        ny = y + dy[direc]
    players[number][0], players[number][1], players[number][2] = nx, ny, direc

# 2. 이동유무 파악하여 대결
def check_player(number):
    x, y, direc, s, cur_gun = players[number]
    is_player = False
    fight_index = -1
    for i in range(M):
        if i != number:
            px, py = players[i][0], players[i][1]
            if px == x and py == y:
                is_player = True
                fight_index = i
                break
    # 2-2-1. 플레이어가 존재하면 싸운다
    if is_player:
        f_x, f_y, f_direc, f_s, f_cur_gun = players[fight_index]
        original_sum = s + cur_gun
        fight_sum = f_s + f_cur_gun
        result = 0
        win_index = 0
        lost_index = 0
        if original_sum == fight_sum:
            if s > f_s:
                win_index = number
                lost_index = fight_index
            else:
                win_index = fight_index
                lost_index = number
        elif original_sum > fight_sum:
            result = original_sum - fight_sum
            win_index = number
            lost_index = fight_index
        else:
            result = fight_sum - original_sum
            win_index = fight_index
            lost_index = number

        points[win_index] += result
        lx, ly, l_d, l_s, l_gun = players[lost_index]
        board[lx][ly].append(l_gun)
        l_gun = 0
        for _ in range(4):
            is_player = False
            nx = lx + dx[l_d]
            ny = ly + dy[l_d]
            for i in range(M):
                if i != lost_index:
                    px, py = players[i][0], players[i][1]
                    if px == nx and py == ny:
                        is_player = True
                        break
            if is_player or nx < 0 or nx >= N or ny < 0 or ny >= N:
                l_d = (l_d + 1) % 4
                continue
            lx, ly = nx, ny
            if len(board[lx][ly]) > 0:
                l_gun = max(board[lx][ly])
                board[lx][ly].remove(l_gun)
            players[lost_index] = [lx, ly, l_d, l_s, l_gun]
            break

        wx, wy, w_d, w_s, w_gun = players[win_index]
        if len(board[wx][wy]) > 0:
            max_gun = max(board[wx][wy])
            if w_gun < max_gun:
                board[wx][wy].append(w_gun)
                w_gun = max_gun
                board[wx][wy].remove(max_gun)
        players[win_index] = [wx, wy, w_d, w_s, w_gun]



    # 2-1. 이동했을 때 플레이어가 없는 경우 총 공격력 최대인 것을 택
    else:
        if len(board[x][y]) > 0:
            max_gun = max(board[x][y])
            if cur_gun < max_gun:
                board[x][y].append(cur_gun)
                cur_gun = max_gun
                board[x][y].remove(cur_gun)
        players[number] = [x, y, direc, s, cur_gun]



N, M, K = map(int, input().split())
players = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(N)]
points = [0] * M
for i in range(N):
    for j in range(N):
        board[i][j] = [board[i][j]]


for _ in range(M):
    x, y, d, s = map(int, input().split())
    players.append([x - 1, y - 1, d, s, 0])

for _ in range(K):
    for i in range(M):
        move_player(i)
        check_player(i)
print(*points)
