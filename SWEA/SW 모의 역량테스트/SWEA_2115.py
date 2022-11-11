# SW Expert Academy - 2115번. [모의 SW 역량테스트] 벌꿀채취

from itertools import combinations


def is_possible(x, y):
    for i in range(M):
        if y + i < N and not visited[x][y + i]:
            continue
        else:
            return False
    return True


def check(cnt):
    global answer
    if cnt == 2:
        total = 0
        for c in range(2):
            result = 0
            for x in range(1, M + 1):
                for comb in combinations(honey[c], x):
                    temp = 0
                    if sum(comb) <= C:
                        for num in comb:
                            temp += (num * num)
                    result = max(result, temp)
            total += result
        answer = max(answer, total)
        return


    for i in range(N):
        for j in range(N):
            if is_possible(i, j):
                for z in range(M):
                    visited[i][j + z] = True
                    honey[cnt].append(board[i][j + z])
                check(cnt + 1)
                for z in range(M):
                    visited[i][j + z] = False
                    honey[cnt].pop()


T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    honey = [[] for _ in range(2)]
    answer = 0
    check(0)
    print('#{} {}'.format(tc, answer))


