# Baekjoon Online Judge - 23288번. 주사위 굴리기 2

from collections import deque


def move(direct):
    if direct == 0:
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    elif direct == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    elif direct == 2:
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    else:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]


def get_score(x, y):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    score = board[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == 0 and board[nx][ny] == score:
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
    return cnt


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = [2, 4, 1, 3, 5, 6] # 마지막 값이 주사위의 밑면
# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direct = 0
x, y = 0, 0
answer = 0
for _ in range(K):
    nx = x + dx[direct]
    ny = y + dy[direct]
    # 1. 주사위 한 칸 이동(범위 벗어날 시 반대로 한 칸)시 방향 설정 및 좌표 구하기
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        direct = (direct + 2) % 4
        nx = x + dx[direct]
        ny = y + dy[direct]
    x, y = nx, ny # 현재 위치 초기화
    move(direct) # 실제로 주사위의 이동
    # 2. bfs를 통해 현재의 값과 같은 개수 구하기
    cnt = get_score(x, y)
    answer += (cnt * board[x][y]) # 점수 누적해서 구하기
    # 3. A(주사위 밑면)와 B(현재 있는 칸의 값)의 비교를 통해 이동 방향 설정(시계 90도 or 반시계 90도 or 변화 X)
    if dice[-1] > board[x][y]:
        direct = (direct + 1) % 4
    elif dice[-1] < board[x][y]:
        direct = (direct - 1) % 4
print(answer)
