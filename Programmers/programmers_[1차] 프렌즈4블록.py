def solution(m, n, board):
    answer = 0
    idxx = 0
    area = [list(item) for item in board]
    # 오른쪽, 아래, 오른쪽아래 대각선
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    while True:
        coor_list = set()
        for x in range(m - 1):
            for y in range(n - 1):
                # 2x2 block이 만들어졌는지 여부
                # 일단 False로 두고
                block = False
                # 0이 아닐 때
                if area[x][y] != 0:
                    # 아니라면 잠재적으로 block 가능성이 있기 때문에 True
                    block = True
                    for z in range(3):
                        nx = x + dx[z]
                        ny = y + dy[z]
                        # 2x2 block이 안만들어졌을 때 False
                        if area[nx][ny] != area[x][y]:
                            block = False
                            break
                # block이 만들어지면 해당 캐릭터에 좌표값 입력
                if block:
                    coor_list.add((x, y))
                    for z in range(3):
                        nx = x + dx[z]
                        ny = y + dy[z]
                        coor_list.add((nx, ny))
        # 모아진 블록을 빈 공간으로 만든다.
        coor_list = list(coor_list)
        for i in range(len(coor_list)):
            area[coor_list[i][0]][coor_list[i][1]] = 0
        # 길이만큼 +
        answer += len(coor_list)

        if len(coor_list) != 0:
            down_list = down(area, n, m)
            area = [item[:] for item in down_list]
        else:
            break

    return answer


# 남아있는 캐릭터들을 구하고 비어있는 공간 제거
def down(arr, n, m):
    temp = [[0] * n for _ in range(m)]
    # 각 열의 남아있는 캐릭터들을 구한다. 밑에서부터
    columns = [[] for _ in range(n)]
    for j in range(n):
        for i in range(m - 1, -1, -1):
            if arr[i][j] != 0:
                columns[j].append(arr[i][j])
    # 값에 넣는다
    for j in range(n):
        idx = m - 1
        for i in range(len(columns[j])):
            temp[idx][j] = columns[j][i]
            idx -= 1
    return temp