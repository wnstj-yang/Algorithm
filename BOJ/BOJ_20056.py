# Baekjoon Online Judge - 20056번. 마법사 상어와 파이어볼

from collections import deque

# 8방향 시계방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    q = deque()
    # board안에 각 좌표들과 안의 값(질량, 속력, 방향)을 q에 넣는다.
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) != 0:
                for z in board[i][j]:
                    q.append((i, j) + z)
                # 각각 좌표들을 알았으니 다 뽑아내고 0으로 초기화
                while len(board[i][j]) != 0:
                    board[i][j].pop()
    # 구한 값들을 통해 이동을 시작한다
    while q:
        r, c, m, s, d = q.popleft()
        nr = (r + dx[d] * s) % N
        nc = (c + dy[d] * s) % N
        # 이동을 완료했을 시 값 추가
        board[nr][nc].append((m, s, d))

    # 이동이 완료된 것들의 조건에 따라 파이어볼 정리
    for i in range(N):
        for j in range(N):
            # 파이어볼이 2개 이상일 때
            if len(board[i][j]) > 1:
                weight, speed, odd, even, cnt = 0, 0, 0, 0, 0
                four_dir = []
                # 주어진 값들의 질량과 속도, 조건에 따라 나눈다
                while board[i][j]:
                    tmp = board[i][j].pop()
                    weight += tmp[0]
                    speed += tmp[1]
                    # 홀수인지 짝수인지 방향을 판단
                    if tmp[2] % 2 == 1:
                        odd += 1
                    else:
                        even += 1
                    cnt += 1
                weight_sum = weight // 5
                speed_sum = speed // cnt
                four_fireball = []
                # 0이면 소멸
                if weight_sum == 0:
                    continue
                # 모두 홀수이거나 짝수인지 판단 (개수로)
                if odd == cnt or even == cnt:
                    four_dir = [0, 2, 4, 6]
                else:
                    four_dir = [1, 3, 5, 7]
                # 각 방향을 계산한 값과 넣는다.
                for z in four_dir:
                    four_fireball.append((weight_sum, speed_sum, z))
                # 4개로 나뉜 것을 현재 위치에 넣음
                board[i][j].extend(four_fireball)


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append((m, s, d))

for _ in range(K):
    move()
result = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for m, s, d in board[i][j]:
                result += m
print(result)

