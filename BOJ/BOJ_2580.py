# Baekjoon Online Judge - 2580번. 스도쿠


def check_row(x, num):
    for j in range(9):
        if sudoku[x][j] == num:
            return False
    return True


def check_col(y, num):
    for i in range(9):
        if sudoku[i][y] == num:
            return False
    return True


def check_square(x, y, num):
    # 3x3 중 첫 번째 위치로 만들 시 3으로 나눈 다음 3으로 곱해준다.
    x = (x // 3) * 3
    y = (y // 3) * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if sudoku[i][j] == num:
                return False
    return True


def search(idx):
    global check

    if not check:
        return
    # 스도쿠 내의 모든 빈 공간을 채웠을 때 끝
    if idx == len(blanks):
        for i in sudoku:
            print(*i)
        check = False
        return

    x, y = blanks[idx][0], blanks[idx][1] # 빈 공간에서의 좌표값
    for j in range(1, 10):
        if check_row(x, j) and check_col(y, j) and check_square(x, y, j):
            # 백트래킹 부분
            sudoku[x][y] = j
            search(idx + 1)
            sudoku[x][y] = 0


sudoku = []
blanks = []
check = True
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blanks.append((i, j))
search(0)
