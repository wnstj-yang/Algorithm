# CODETREE 2022 상반기 오전 2번 - 예술성

from collections import deque


def comb(idx, k):
    if k == 2:
        candis.append(list(candi))
        return

    for i in range(idx, len(groups)):
        if not visited[i]:
            visited[i] = True
            candi[k] = numbers[i]
            comb(i, k + 1)
            visited[i] = False


def bfs():
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                q = deque()
                q.append((i, j))
                num = board[i][j]
                group = [num, [(i, j)]]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if not visited[nx][ny] and board[nx][ny] == num:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            group[1].append((nx, ny))
                groups.append(group)


def compare_groups(a, b):
    group_A = groups[a]
    group_B = groups[b]
    num_A, num_B = group_A[0], group_B[0] # 맨 앞에 값을 나타낸다.
    borders = 0
    for x, y in group_A[1]:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if (nx, ny) in group_B[1]: #
                borders += 1
    return (len(group_A[1]) + len(group_B[1])) * borders * num_A * num_B


def turn():
    temp = [[0] * N for _ in range(N)]
    # 십자가 반시계 방향 90도 회전
    # 1. 세로 줄의 경우 가로로 옮기기
    for idx in range(N):
        temp[N // 2][idx] = board[idx][N // 2]

    # 2. 가로 줄의 경우 세로로 옮기기
    for idx in range(N):
        temp[N - idx - 1][N // 2] = board[N // 2][idx]

    # 1. 왼쪽 상단 네모
    for x in range(0, N // 2):
        for y in range(0, N // 2):
            temp[y][N // 2 - 1 - x] = board[x][y]

    # 2. 오른쪽 상단 네모
    for x in range(N // 2):
        idx = 0
        for y in range(N // 2 + 1, N):
            temp[idx][N - 1 - x] = board[x][y]
            idx += 1
    # 3. 왼쪽 하단 네모
    idx = 0
    for x in range(N // 2 + 1, N):
        for y in range(N // 2):
            temp[N // 2 + 1 + y][N // 2 - 1 - idx] = board[x][y]
        idx += 1
    # 4. 오른쪽 하단 네모
    idx = 0
    for x in range(N // 2 + 1, N):
        for y in range(N // 2 + 1, N):
            temp[y][N - 1 - idx] = board[x][y]
        idx += 1

    return temp


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for z in range(4):
    result = 0
    groups = [] # 만들어지는 그룹들을 넣을 리스트
    bfs()
    candis = [] # 한 쌍의 후보들을 조합으로 구한다.
    candi = [0] * 2
    visited = [False] * len(groups)
    numbers = list(range(len(groups)))
    comb(0, 0)
    for temp in candis:
        result += compare_groups(temp[0], temp[1])
    answer += result
    board = turn()
print(answer)


