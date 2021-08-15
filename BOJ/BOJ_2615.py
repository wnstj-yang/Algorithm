# Baekjoon Online Judge - 2615. 오목
# 조건 생각이 어려웠다

# 4방향 (좌하, 하, 우하, 우) => 오목판에서 왼쪽에서 오른쪽으로 탐색하기 때문
dx = [1, 1, 1, 0]
dy = [-1, 0, 1, 1]


# 앞에서부터 2개는 좌표, 2개는 방향, 마지막은 흑백 구분
def check(x, y, a, b, stone):
    global found_ans
    cnt = 1
    # 첫 좌표의 값을 저장한다. 오목일 때 육목 체크 위함
    first_x = x
    first_y = y
    # 오목 가능성이 있는 좌표들을 저장
    get_coor = [(x, y)]
    while True:
        # 육목이상이면 그냥 끝 더이상 안본다
        if cnt >= 6:
            return
        nx = x + a
        ny = y + b
        if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            break
        else:
            # 같은 바둑돌이라면
            if board[nx][ny] == stone:
                get_coor.append((nx, ny))
                # 이후 값을 변경
                x = nx
                y = ny
                cnt += 1
            else:
                break
    # 오목이다?
    if cnt == 5:
        # 오목의 첫 좌표값에서 반대방향으로 1개 체크 후 같으면 육목이니 return
        nx = first_x - a
        ny = first_y - b
        if (0 <= nx < 19 and 0 <= ny < 19) and board[nx][ny] == stone:
            return
        found_ans = True
        return get_coor


def find_path(x, y, color):
    global found_ans, ans_color
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            continue
        else:
            if board[nx][ny] == color:
                temp = check(x, y, dx[i], dy[i], color)
                if found_ans:
                    ans_color = color
                    # 방향이 좌하일 때 좌표값들 중 마지막이 가장 왼쪽이다
                    if i == 0:
                        ans_x, ans_y = temp[-1]
                        return ans.append((ans_x+1, ans_y+1))
                    else:
                        return ans.append((x+1, y+1))


board = [list(map(int, input().split())) for _ in range(19)]
ans = []
ans_color = 0
found_ans = False

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            find_path(i, j, board[i][j])
            if found_ans:
                break
    if found_ans:
        break

if ans:
    print(ans_color)
    print(ans[0][0], ans[0][1])
else:
    print(ans_color)
