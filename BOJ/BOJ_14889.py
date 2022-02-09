# Baekjoon Online Judge - 스타트와 링크
# pypy로 시간 줄음
# import sys
# input = sys.stdin.readline


def combi(idx, k):
    # 조합으로 모아진 수들을 담아넣는다
    if idx == N // 2:
        ans_list.append(list(ans))
        return

    for i in range(k, N):
        if not visited[i]:
            visited[i] = True
            ans[idx] = i
            combi(idx + 1, i)
            visited[i] = False


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [False] * N
ans = [0] * (N // 2) # 조합 경우의 수 구할 때 숫자 넣는 리스트
ans_list = [] # 조합 리스트
combi(0, 0)
min_val = 987654321
for team_start in ans_list:
    # 스타트 팀 사람들과 이를 제외한 링크 팀
    team_link = [i for i in range(N) if i not in team_start]
    start, link = 0, 0 # 각각 능력치의 합
    for i in range(len(team_start) - 1):
        x = team_start[i]
        for j in range(i + 1, len(team_start)):
            y = team_start[j]
            start += (board[x][y] + board[y][x])

    for i in range(len(team_link) - 1):
        x = team_link[i]
        for j in range(i + 1, len(team_link)):
            y = team_link[j]
            link += (board[x][y] + board[y][x])
    # 두 팀의 능력치를 절대값으로 빼서 최소값을 구한다.
    min_val = min(min_val, abs(start - link))
print(min_val)

