# Baekjoon Online Judge - 15684번. 사다리 조작
import sys
input = sys.stdin.readline


def check():
    for j in range(1, N + 1):
        current = j # 현재 세로선에서의 위치
        for i in range(1, H + 1):
            # 밑으로내려가는데 가로선이 있다? 그러면 오른쪽으로 이동
            if ladders[i][current] == 1:
                current += 1
            # 밑으로 내려가는데 왼쪽에 가로선이 있다? 그러면 왼쪽으로 이동
            elif ladders[i][current - 1] == 1:
                current -= 1
        # 다 내려와서 같은 세로선의 위치가 아니라면 끝
        if current != j:
            return False
    return True


def dfs(cnt, idx, target):
    global answer
    # 추가할 수 있는 가로선의 개수만큼 만들어진 경우 체크
    if cnt == target:
        if check():
            answer = min(answer, cnt)
        return
    # idx를 통해 조합형식으로 가로선들을 정한다
    for j in range(idx, N):
        for i in range(1, H + 1):
            if ladders[i][j] == 0 and ladders[i][j - 1] == 0 and ladders[i][j + 1] == 0:
                ladders[i][j] = 1
                dfs(cnt + 1, j, target)
                ladders[i][j] = 0


N, M, H = map(int, input().split())
ladders = [[0] * (N + 1) for _ in range(H + 1)]
visited = [[False] * (N + 1) for _ in range(H + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    ladders[x][y] = 1
answer = 987654321
# 최대 3개 가로선을 그을 수 있기 때문에 개수에 따른 dfs
for i in range(4):
    dfs(0, 0, i)
    # 순서대로 0, 1, 2, 3개를 정하기 때문에 사다리 조작이 완료되면 끝
    if answer != 987654321:
        print(answer)
        break
if answer == 987654321:
    print(-1)
