# SW Expert Academy - 1961 숫자 배열 회전

# 90도 돌릴 때 리스트들을 업데이트 한다.
def rotate(arr):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][N - i - 1] = arr[i][j]

    return temp


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = [[0] * 3 for _ in range(N)]
    for j in range(3):
        board = rotate(board)
        for i in range(N):
            result[i][j] = ''.join(map(str, board[i]))
    board = rotate(board)
    print('#{}'.format(tc))
    for i in result:
        print(*i)

