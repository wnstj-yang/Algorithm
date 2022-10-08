# Baekjoon Online Judge - 16235번. 나무 재테크

from collections import deque
import sys
input = sys.stdin.readline


# 봄과 여름 같이 진행
def spring_summer():
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                length = len(trees[i][j])
                for k in range(length):
                    if nourish[i][j] >= trees[i][j][k]:
                        nourish[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
                    else:
                        # 여름 부분이며 죽은 나무들을 2로 나눈 값들이 양분으로 된다
                        for _ in range(k, length):
                            nourish[i][j] += trees[i][j].pop() // 2
                        break


# 가을과 겨울을 합쳐서 진행
def fall_winter():
    for i in range(N):
        for j in range(N):
            nourish[i][j] += winter[i][j]
            if trees[i][j]:
                for k in range(len(trees[i][j])):
                    if trees[i][j][k] % 5 == 0:
                        for z in range(8):
                            nx = i + dx[z]
                            ny = j + dy[z]
                            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                                continue
                            # deque를 활용해 맨 앞에 나이 1인 나무를 추가해줘서 시간을 줄인다.
                            trees[nx][ny].appendleft(1)


N, M, K = map(int, input().split())
nourish = [[5] * N for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
winter = [list(map(int, input().split())) for _ in range(N)]
result = 0
# 8방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)


for _ in range(K):
    spring_summer()
    fall_winter()

for i in range(N):
    for j in range(N):
        result += len(trees[i][j])

print(result)
