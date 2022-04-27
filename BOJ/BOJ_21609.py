# Baekjoon Online Judge - 21609번. 상어 중학교

from collections import deque


def search_group(x, y, val):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    group = [(x, y)]
    visited[x][y] = True
    cnt = 1
    rainbow_cnt = 0
    rainbows = []
    result = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[nx][ny] and (board[nx][ny] == val or board[nx][ny] == 0):
                visited[nx][ny] = True
                q.append((nx, ny))
                if board[nx][ny] == 0:
                    rainbow_cnt += 1
                    cnt += 1
                    rainbows.append((nx, ny))
                else:
                    cnt += 1
                    group.append((nx, ny))
    # 무지개 블록의 경우 방문 표시 된 것을 다시 풀어주어야한다.(무지개 블록은 얼마나 들어있든 상관 없음)
    for x, y in rainbows:
        visited[x][y] = False
    if cnt > 1:
        group.sort(key=lambda x: (x[0], x[1]))
        # 기준이 행이 가장 작고 열이 가장 작은 것
        # 근데 행이 가장 작은 것이 여러 개 있다면 열의 번호가 가장 작은 블록을 택한다.
        # 즉, 그냥 행과 열 둘다 가장 작은 것을 택한다.
        # 블록의 개수, 무지개 블록의 개수, 기준 블록의 x, y 좌표(각각), 일반과 무지개 블록들의 좌표들을 리스트로 만든 후 반환
        result = [cnt, rainbow_cnt, group[0][0], group[0][1], group + rainbows]
    return result


# 가장 큰 블록안의 좌표를 구해서 빈 칸으로 만든다.
def remove_blocks(arr):
    for x, y in arr:
        board[x][y] = 6


# 반시계 방향으로 90도
def rotate_blocks_90():
    global board
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][i] = board[i][N - 1 - j]
    board = temp


def gravitiy():
    global board
    for j in range(N):
        blank = 0
        for i in range(N - 1, -1, -1):
            # 검은색 블록인 경우 빈 칸 수 초기화
            if board[i][j] == -1:
                blank = 0
            # 빈 칸이라면 개수 증가
            elif board[i][j] == 6:
                blank += 1
            else:
                # 일반 블록일 때 빈칸 개수가 1개 이상이면 그 만큼 중력에 의해 일반 블록을 아래로 내린다
                if blank > 0:
                    board[i + blank][j] = board[i][j]
                    board[i][j] = 6


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
while True:
    groups = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and (0 < board[i][j] < M + 1):
                result = search_group(i, j, board[i][j])
                if len(result) != 0:
                    groups.append(result)
    if len(groups) == 0:
        break

    # 아래와 같이 내림차순 정렬로 했을 때 조건에 맞게 가장 큰 블록 그룹을 선택할 수 있다.
    groups.sort(reverse=True)
    big_group = groups[0]
    # 1. 가장 큰 블록을 찾았으니 값을 제거해준다
    # 2. 제거 이후 점수를 획득한 이후에 중력작용
    # 3. 반시계방향으로 90도 회전
    # 4. 중력 적용
    remove_blocks(big_group[-1])
    answer += big_group[0] ** 2
    gravitiy()
    rotate_blocks_90()
    gravitiy()

print(answer)
