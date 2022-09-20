# SW Expert Academy - 1974번. 스도쿠 검증

T = int(input())

for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    check = False
    # 3x3 간격으로 1~9사이에 값이 겹치는 것이 있다면 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = [1] * 10
            for x in range(3):
                for y in range(3):
                    cnt[board[x + i][y + j]] -= 1
            if 1 in cnt[1:]:
                check = True
                break
        if check:
            break
    if check:
        print('#{} 0'.format(tc))
        continue
    # 세로로 판단
    check = False
    for i in range(9):
        cnt = [1] * 10
        for j in range(9):
            cnt[board[i][j]] -= 1
        if 1 in cnt[1:]:
            check = True
            break
    if check:
        print('#{} 0'.format(tc))
        continue
    # 가로로 판단
    for j in range(9):
        cnt = [1] * 10
        for i in range(9):
            cnt[board[i][j]] -= 1
        if 1 in cnt[1:]:
            check = True
            break
    if check:
        print('#{} 0'.format(tc))
        continue
    print('#{} 1'.format(tc))


