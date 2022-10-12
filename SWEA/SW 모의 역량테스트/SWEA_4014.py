# SW Expert Academy - 4014번. [모의 SW 역량테스트] 활주로 건설


def check(line):
    visited = [False] * N
    for i in range(N - 1):
        num = abs(line[i] - line[i + 1])
        # 높이가 1 차이 날 때 다시 계산해서 1이면 오르막길 활주로, -1이면 내리막길 활주로로 파악
        if num == 1:
            if line[i] - line[i + 1] == 1:
                #
                for j in range(X):
                    if i + j + 1 >= N or visited[i + j + 1] or line[i + 1] != line[i + j + 1]:
                        return False

                    elif line[i + 1] == line[i + j + 1]:
                        visited[i + j + 1] = True
            else:
                #
                for j in range(X):
                    if i - j < 0 or visited[i - j] or line[i] != line[i - j]:
                        return False

                    elif line[i - j] == line[i]:
                        visited[i - j] = True
        elif num > 1:
            return False
    return True


T = int(input())

for tc in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for line in board:
        if check(line):
            result += 1
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(board[i][j])
        if check(temp):
            result += 1
    print('#{} {}'.format(tc, result))
