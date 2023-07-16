# Baekjoon Online Judge - 10703번. 유성
# 기존에 BFS로 진행해서 리스트들에 대해서 초기화를 하다보니 시간 초과
# 열로 반복문 순회를 하면서 유성 조각과 땅 사이 거리의 최소를 구해서 옮긴다


import sys

input = sys.stdin.readline


R, S = map(int, input().split())
board = [list(input()) for _ in range(R)]
arr = [['.'] * S for _ in range(R)] # 추후 땅과 유성조각을 넣는다
dx = [-1, 1, 0, 0] # 4방향 상하좌우
dy = [0, 0, -1, 1]

cnt = 987654321 # 유성과 땅 사이의 거리
# 행과 열 중 열을 기준으로 파악한다.
for j in range(S):
    max_star = 0 # 유성이 나타났을 때 최대 행 인덱스
    min_ground = R - 1 # 땅이 나타났을 때 최소 인덱스
    flag = False # 유성이 나타났는지 확인
    for i in range(R):
        if board[i][j] == 'X':
            max_star = max(max_star, i)
            flag = True
        elif board[i][j] == '#':
            min_ground = min(min_ground, i)
    # 각 열을 돌면서 최소값을 구한다.
    if flag:
        cnt = min(cnt, abs(max_star - min_ground) - 1)

# '.'로 초기화된 리스트에서 유성과 땅을 기존에 입력받는 것을 바탕으로 넣는다
# 유성조각을 행과 거리를 더한 곳을 넣는다
for i in range(R):
    for j in range(S):
        if board[i][j] == 'X':
            arr[i + cnt][j] = 'X'
        if board[i][j] == '#':
            arr[i][j] = '#'

# 최대한 print로 일어나는 시간을 줄이는 방법
for i in range(R):
    for j in range(S):
        sys.stdout.write(arr[i][j])
    sys.stdout.write('\n')
