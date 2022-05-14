# Baekjoon Online Judge - 10159번. 저울

N = int(input())
M = int(input())
board = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    board[x][y] = True

# 플로이드 와샬 방법을 통해 무게 비교가 가능하다면 True로 체크
# Ex) 1 > 2, 2 > 3일 때 1 > 3이 비교가 가능하다
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][k] and board[k][j]:
                board[i][j] = True

for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if i != j:
            # i -> j, j -> i 하는 이유는 시작점이 달라도 비교가 가능할 수 있기 때문에
            # 정답처리 시 비교가 안되는 부분을 찾아야하므로 아래와 같이 조건을 걸어야 한다.
            if not board[i][j] and not board[j][i]:
                cnt += 1
    print(cnt)
