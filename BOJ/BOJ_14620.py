# Baekjoon Online Judge - 14620번. 꽃길

from itertools import combinations


# item : 조합의 경우의 수인 3개의 좌표값
def check(item):
    visited = [[False] * N for _ in range(N)] # 방문 표시로 겹치는 꽃잎이 있는지 파악
    cnt = 0 # 꽃이 피어진 비용
    for x, y in item:
        cnt += board[x][y] # 씨앗이 위치한 곳에 대한 비용
        visited[x][y] = True # 씨앗의 위치 방문
        for i in range(4):
            nx = x + dx[i] # 현재 x좌표에서 4방향 더한 값
            ny = y + dy[i] # 현재 y좌표에서 4방향 더한 값
            if visited[nx][ny]: # 방문한 곳이라면 꽃잎이 겹치므로 -1이란 값으로 죽은 꽃을 의미
                return -1
            visited[nx][ny] = True # 꽃잎의 위치를 방문 표시로 구분
            cnt += board[nx][ny] # 꽃잎의 위치에 대한 비용 추가
    return cnt # 세 개의 꽃이 다 피어난 이후의 비용을 반환한다


# 상하좌우 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)] # 화단
candis = [] # 세 씨앗에 대한 조합의 결과를 넣을 리스트
ans = 987654321 # 최소값을 구해야 하므로 일종의 최대값을 지정
# (1, 1) ~ (N - 1, N - 1)로 반복문을 도는 이유는 씨앗에서 상하좌우로 펼쳐지기 때문에
# 왼쪽 상단 끝점에서 1칸씩, 오른쪽 하단에서 1칸씩 앞당기고 줄여서 범위를 벗어나지않게 조정
for i in range(1, N - 1):
    for j in range(1, N - 1):
        candis.append((i, j)) # 범위에 해당하는 좌표값들을 넣어준다
for candi in combinations(candis, 3): # 각 좌표값들에 대해 씨앗이 3개인 조합을 구한다
    result = check(candi)  # 3개의 조합이 된 결과를 통해 점검한다
    if result != -1: # -1이면 꽃잎이 겹친 것이므로 -1이 아니라면 최소 비용을 비교한다.
        ans = min(result, ans)
print(ans)
