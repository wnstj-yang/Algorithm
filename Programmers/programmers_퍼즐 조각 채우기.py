def dfs(tables, x, y, length, num, coor):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    puzzle = [coor] # 퍼즐 조각에 대한 좌표값들 저장
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= length or ny < 0 or ny >= length:
            continue
        else:
            if tables[nx][ny] == num:
                tables[nx][ny] = 2
                # 퍼즐 조각에 대한 좌표값을 dfs하면서 저장을 시켜놓는다 ( 지속 초기화 )
                # 예를 들어, 1 1 1 이렇게 있으면 마지막의 1부터 첫 번째 1까지의 좌표를 더해준다
                puzzle = puzzle + dfs(tables, nx, ny, length, num, [coor[0] + dx[i], coor[1] + dy[i]])
    # 마지막에 만들어진 퍼즐 조각 전체 좌표를 반환한다.
    return puzzle


# 90도 회전 로직
def rotate(arr, row, col):
    temp_table = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            temp_table[j][row - i - 1] = arr[i][j]
    return temp_table


def solution(game_board, table):
    answer = 0
    blocks = []
    row = len(game_board)
    col = len(game_board[0])
    # 게임 보드 안의 블록들의 좌표 값들을 0,0부터 시작한 것들을 구한다.
    for i in range(row):
        for j in range(col):
            if game_board[i][j] == 0:
                game_board[i][j] = 2
                result = dfs(game_board, i, j, row, 0, [0, 0])
                blocks.append(result)
    # 게임 보드 안의 각 블록들에 대한 정보 저장

    # table을 90도씩 4번 회전하여 각 퍼즐 조각을 회전한다.
    for t in range(4):
        table = rotate(table, row, col)
        copy_table = [item[:] for item in table]
        for k in copy_table:
            print(*k)
        for i in range(row):
            for j in range(col):
                # 조각이 될 가능성이 있는것이라면 블록과 조각이 맞는지 체크
                if copy_table[i][j] == 1:
                    copy_table[i][j] = 2
                    # 회전해서 좌표값이 다르므로, 0, 0부터시작해서 각각에 대한 좌표를 구한다.
                    # 매개변수와 연결되므로 초기화됨
                    result = dfs(copy_table, i, j, row, 1, [0, 0])
                    # 만들어진 하나의 조각에 대한 좌표값들이 블록과 맞는 것이 있는지 체크한다.
                    if result in blocks:
                        # 존재할 시 블록에 맞게 들어간 것이므로 블록 리스트내에서 제거함
                        blocks.pop(blocks.index(result))
                        # 총 길이를 더한다
                        answer += len(result)
                        # 조각이 맞추어진다면 table을 초기화해준다
                        table = [item[:] for item in copy_table]
                    else:
                        # 블록과 맞는 것이 없다면 이전의 table로 초기화
                        copy_table = [item[:] for item in table]

    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
